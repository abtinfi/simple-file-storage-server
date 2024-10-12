from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
import os

app = FastAPI()

UPLOAD_DIRECTORY = "./files"

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)


@app.post("/files/{name}")
async def upload_file(name: str, file: UploadFile = File(...)):
    # TODO: Check if a file with the same name already exists and handle duplicates appropriately.
    # TODO: Add error handling for unsupported file types or sizes (e.g., limit file size to prevent excessive storage use).
    pass

@app.delete("/files/{name}")
async def delete_file(name: str):
    # TODO: Implement a soft-delete mechanism to allow file recovery.
    # TODO: Log deletion actions for audit purposes or add permission checks for file deletion.
    pass


@app.get("/files", response_model=List[str])
async def list_files():
    # TODO: Sort files by name, date, or other attributes for improved organization.
    # TODO: Implement pagination if the number of files grows large to handle listing performance.
    pass