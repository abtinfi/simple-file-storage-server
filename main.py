from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
import os

app = FastAPI()

UPLOAD_DIRECTORY = "./files"

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@app.post("/files/{name}")
async def upload_file(name: str, file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIRECTORY, name)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    return {"message": f"File '{name}' uploaded successfully"}

@app.delete("/files/{name}")
async def delete_file(name: str):
    file_path = os.path.join(UPLOAD_DIRECTORY, name)
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail=f"File '{name}' not found")
    os.remove(file_path)
    return {"message": f"File '{name}' deleted successfully"}

@app.get("/files", response_model=List[str])
async def list_files():
    files = [f for f in os.listdir(UPLOAD_DIRECTORY) if os.path.isfile(os.path.join(UPLOAD_DIRECTORY, f))]
    return files
