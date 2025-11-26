import json
from app import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert b"API Flask - Quishpe" in res.data 

def test_predict_get():
    client = app.test_client()
    res = client.get("/predict?text=hola")
    data = res.get_json()
    assert data["score"] == 4
    assert data["input"] == "hola"

def test_predict_post():
    client = app.test_client()
    res = client.post("/predict", json={"text": "test"})
    data = res.get_json()
    assert data["score"] == 4
    assert data["input"] == "test"
