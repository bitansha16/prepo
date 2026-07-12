from fastapi import FastAPI, UploadFile, File, Form
from pypdf import PdfReader
from gemini_service import analyze_resume, ats_analysis, recommend_jobs, generate_interview, generate_dsa_roadmap
import tempfile


app = FastAPI()


def extract_pdf_text(file_content):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        temp.write(file_content)
        path = temp.name

    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text


@app.get("/")
def home():

    return {
        "project": "Prepo",
        "message": "AI Interview Preparation & Career Assistant"
    }


@app.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    content = await file.read()

    resume_text = extract_pdf_text(content)

    analysis = analyze_resume(resume_text)

    return {
        "filename": file.filename,
        "analysis": analysis
    }


@app.post("/ats-check")
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
@app.post("/recommend-jobs")
async def job_recommendation(
    file: UploadFile = File(...)
):

    content = await file.read()

    resume_text = extract_pdf_text(content)

    result = recommend_jobs(resume_text)

    return {
        "filename": file.filename,
        "recommendations": result
    }
@app.post("/mock-interview")
async def mock_interview(
    file: UploadFile = File(...)
):

    content = await file.read()


    resume_text = extract_pdf_text(content)


    questions = generate_interview(
        resume_text
    )


    return {

        "filename":file.filename,

        "interview_questions":questions

    }
@app.post("/dsa-roadmap")
async def dsa_roadmap(
    level: str,
    target: str
):

    roadmap = generate_dsa_roadmap(
        level,
        target
    )


    return {

        "level":level,

        "target":target,

        "roadmap":roadmap

    }