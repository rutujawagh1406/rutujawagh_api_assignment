import os
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine
import shutil

client = TestClient(app)

def setup_module(module):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    shutil.rmtree("uploads", ignore_errors=True)

def test_post_and_get():
    file_content = b"dummy file"
    response = client.post(
        "/api/forms/wheel-specifications",
        data={
            "formNumber": "KPA-999",
            "submittedBy": "Test User",
            "fields": '{"a":1, "b":2}'
        },
        files={"file": ("test.txt", file_content)},
    )
    assert response.status_code == 200
    data = response.json()
    form_id = data["id"]

    get_resp = client.get(f"/api/forms/wheel-specifications/{form_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["submittedBy"] == "Test User"
