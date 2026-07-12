from fastapi import APIRouter, UploadFile, File

from app.services.pdf_service import extract_pdf_text

from app.services.gemini_service import recommend_jobs


router = APIRouter()



@router.post("/recommend-jobs")
async def job_recommendation(
    file: UploadFile = File(...)
):

    content = await file.read()


    resume_text = extract_pdf_text(content)


    result = recommend_jobs(
        resume_text
    )


    return {

        "filename": file.filename,

        "recommendations": result

    }