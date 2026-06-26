import os
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI(title="ManyChat AI Bridge")

class WebhookPayload(BaseModel):
    user_id: str
    last_input: str
    context: dict = {}

@app.get("/")
async def root():
    return {"status": "online", "bridge": "ManyChat to Anthropic Claude"}

@app.post("/webhook/manychat")
async def handle_manychat_webhook(payload: WebhookPayload):
    """
    Receives incoming messaging events from platforms like ManyChat
    and formats them for processing via the Anthropic API.
    """
    if not payload.last_input:
        raise HTTPException(status_code=400, detail="Missing user input string.")
        
    # Placeholder structure for Claude Context processing
    processed_response = {
        "user_id": payload.user_id,
        "received_message": payload.last_input,
        "status": "Ready for Claude API routing"
    }
    
    return processed_response
