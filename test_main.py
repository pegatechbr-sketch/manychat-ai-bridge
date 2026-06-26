from fastapi.testclient import TestClient
from main import app

# Inicializa o cliente de teste nativo do FastAPI
client = TestClient(app)

def test_read_root():
    """
    Testa se o ponto de entrada principal do servidor está online e ativo.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "online", "bridge": "ManyChat to Anthropic Claude Active"}

def test_handle_manychat_webhook_success():
    """
    Testa o envio de uma carga de dados válida do ManyChat simulando a conversa de um lead.
    """
    payload = {
        "user_id": "123456789",
        "last_input": "Olá, gostaria de saber mais sobre as automações de vídeo.",
        "context": {"platform": "instagram"}
    }
    response = client.post("/webhook/manychat", json=payload)
    assert response.status_code == 200
    
    data = response.json()
    assert data["user_id"] == "123456789"
    assert "reply" in data
    assert "automation_actions" in data

def test_handle_manychat_webhook_missing_input():
    """
    Testa o comportamento de segurança do sistema caso o ManyChat envie um payload sem texto.
    """
    invalid_payload = {
        "user_id": "123456789",
        "last_input": "",
        "context": {}
    }
    response = client.post("/webhook/manychat", json=invalid_payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Missing user input string."
