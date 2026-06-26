import os
import anthropic

class ClaudeBridgeClient:
    def __init__(self):
        # Inicializa o cliente usando a chave de API das variáveis de ambiente
        self.client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", "mock_key_for_testing"))
        self.model = "claude-3-5-sonnet-20241022"

    def generate_response(self, user_message: str, conversation_history: list = None) -> dict:
        """
        Processa a mensagem do ManyChat, aplica o tom de voz do negócio
        e gerencia fluxos condicionais (como envio de vídeos/links).
        """
        if conversation_history is None:
            conversation_history = []

        # Configuração do comportamento do agente de negócios
        system_prompt = (
            "You are an advanced digital business assistant. Your goal is to guide leads through "
            "automated funnels with a helpful, engaging, and professional tone. "
            "If the user shows strong intent or asks for a video/demonstration, you must include the "
            "keyword [TRIGGER_VIDEO_FLOW] at the end of your response so our system can route the asset."
        )

        # Monta a estrutura de mensagens para a API do Claude
        messages = conversation_history + [
            {"role": "user", "content": user_message}
        ]

        try:
            # Chamada oficial do SDK da Anthropic
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                system=system_prompt,
                messages=messages
            )
            
            ai_text = response.content[0].text
            
            # Lógica de Roteamento Inteligente (Smart Routing)
            trigger_video = "[TRIGGER_VIDEO_FLOW]" in ai_text
            clean_text = ai_text.replace("[TRIGGER_VIDEO_FLOW]", "").strip()

            return {
                "response_text": clean_text,
                "trigger_video_automation": trigger_video,
                "status": "success"
            }

        except Exception as e:
            return {
                "response_text": "Desculpe, ocorreu um erro ao processar sua solicitação.",
                "trigger_video_automation": False,
                "status": f"error: {str(e)}"
            }
