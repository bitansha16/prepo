from fastapi import APIRouter, UploadFile, File

from app.services.pdf_service import extract_pdf_text

from app.services.gemini_service import generate_interview



router = APIRouter()



@router.post("/mock-interview")
async def mock_interview(
    file: UploadFile = File(...)
):

    content = await file.read()


    resume_text = extract_pdf_text(
        content
    )


    questions = generate_interview(
        resume_text
    )


    return {

        "filename": file.filename,

        "interview_questions": questions

    }