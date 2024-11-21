from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.services.ocr_service import process_image

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

@app.post("/upload")
async def upload_receipt(file: UploadFile = File(...)):
    processed_file = process_image(file)
    return {"message": "File uploaded successfully!"}
