from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    """test_read_main"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Wikipedia API. Call /search, /wiki or /phrase"
    }


def test_read_phrase():
    """test_read_phrase"""
    response = client.get("/phrase/Barack Obama")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "barack hussein obama ii",
            "bə-rahk hoo-sayn oh-bah-mə",
            "august",
            "american politician",
            "44th president",
        ]
    }
