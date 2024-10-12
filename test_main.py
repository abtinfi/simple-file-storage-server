import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_upload_file():
    file_name = "test_file.txt"
    file_content = b"Hello, this is a test file."

    response = client.post(
        f"/files/{file_name}",
        files={"file": (file_name, file_content, "text/plain")}
    )
    assert response.status_code == 200
    assert response.json() == {"message": f"File '{file_name}' uploaded successfully"}

def test_list_files_after_upload():
    response = client.get("/files")
    assert response.status_code == 200
    assert "test_file.txt" in response.json()

def test_delete_file():
    file_name = "test_file.txt"

    response = client.delete(f"/files/{file_name}")
    assert response.status_code == 200
    assert response.json() == {"message": f"File '{file_name}' deleted successfully"}

def test_list_files_after_delete():
    response = client.get("/files")
    assert response.status_code == 200
    assert "test_file.txt" not in response.json()
