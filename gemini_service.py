import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)



def analyze_resume(resume_text):

    prompt = f"""
    You are an expert resume analyzer.

    Analyze the following resume.

    Provide:

    1. Skills
    2. Technologies
    3. Education
    4. Projects
    5. Strengths
    6. Weakness
    7. Improvement Suggestions


    Resume:

    {resume_text}
    """

    response = model.generate_content(prompt)

    return response.text





def ats_analysis(resume_text, job_description):

    prompt = f"""

    You are an ATS (Applicant Tracking System).

    Compare the resume with the job description.


    Return:

    ATS Score out of 100

    Matching Skills

    Missing Skills

    Missing Keywords

    Resume Improvement Suggestions


    Resume:
    {resume_text}



    Job Description:

    {job_description}

    """


    response = model.generate_content(prompt)


    return response.text
def recommend_jobs(resume_text):

    prompt = f"""
    You are an AI Career Advisor.

    Analyze the candidate resume.

    Recommend suitable career paths.

    Return:

    1. Suitable Job Roles
    2. Match Percentage
    3. Reason for Recommendation
    4. Missing Skills
    5. Skills to Learn
    6. Suggested Projects


    Resume:

    {resume_text}

    """

    response = model.generate_content(prompt)

    return response.text

def generate_interview(resume_text):

    prompt=f"""

    You are a senior technical interviewer.

    Analyze this resume.

    Generate interview preparation questions.

    Include:

    1. Technical Questions
    2. Project Based Questions
    3. DSA Questions
    4. HR Questions
    5. Expected Answer Points


    Resume:

    {resume_text}

    """


    response=model.generate_content(prompt)


    return response.text
def generate_dsa_roadmap(level, target):

    prompt=f"""

    You are an expert Software Engineering mentor.

    Create a personalized DSA preparation roadmap.


    Candidate Level:
    {level}


    Target:
    {target}


    Generate:

    1. Complete weekly roadmap
    2. Topics order
    3. Important concepts
    4. Leetcode problems
    5. Difficulty level
    6. Time required
    7. Interview preparation tips


    Make it practical for cracking FAANG and top tech companies.

    """


    response=model.generate_content(prompt)


    return response.text