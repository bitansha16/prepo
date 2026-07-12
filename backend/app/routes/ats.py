from fastapi import APIRouter, UploadFile, File, Form

from app.services.pdf_service import extract_pdf_text

from app.services.gemini_service import ats_analysis


router = APIRouter()



@router.post("/ats-check")
async def ats_checker(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    content = await file.read()


    resume_text = extract_pdf_text(content)


    result = ats_analysis(
        resume_text,
        job_description
    )


    return {

        "filename": file.filename,

        "ATS_Result": result

    }