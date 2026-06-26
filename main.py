import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from claude_client import ClaudeBridgeClient

app = FastAPI(title="ManyChat AI Bridge")

# Inicializa o conector do Claude
claude_bridge = ClaudeBridgeClient()

class WebhookPayload(BaseModel):
    user_id: str
    last_input: str
    context: dict = {}

@app.get("/")
async def root():
    return {"status": "online", "bridge": "ManyChat to Anthropic Claude Active"}

@app.post("/webhook/manychat")
async def handle_manychat_webhook(payload: WebhookPayload):
    """
    Recebe o evento de mensagem do ManyChat, envia para o processamento do Claude
    e retorna a resposta estruturada junto com gatilhos de automação de vídeo.
    """
    if not payload.last_input:
        raise HTTPException(status_code=400, detail="Missing user input string.")
    
    # Processa a mensagem usando o motor inteligente do Claude
    result = claude_bridge.generate_response(user_message=payload.last_input)
    
    # Se o Claude identificar intenção de assistir a um conteúdo, o sistema injeta a automação
    video_url = None
    if result["trigger_video_automation"]:
        # Simulação de busca de link de vídeo personalizado baseado no contexto
        video_url = "https://yourplatforms.com/assets/delivery-video-01.mp4"

    return {
        "user_id": payload.user_id,
        "reply": result["response_text"],
        "automation_actions": {
            "send_video": result["trigger_video_automation"],
            "video_target_url": video_url
        },
        "meta": {"engine": "Claude 3.5 Sonnet", "status": result["status"]}
    }
