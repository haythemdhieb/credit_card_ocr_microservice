from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.post("/process_file/", response_model=dict)
async def create_upload_file(file_id, file: UploadFile):
    return {"filename": file_id}
