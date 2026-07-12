from fastapi import APIRouter, UploadFile, File

from app.services.pdf_service import extract_pdf_text

from app.services.gemini_service import analyze_resume



router = APIRouter()



@router.post("/upload-resume")
async def upload_resume(
    file:UploadFile=File(...)
):

    content=await file.read()


    text=extract_pdf_text(content)


    result=analyze_resume(text)


    return {

        "filename":file.filename,

        "analysis":result

    }