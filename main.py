from fastapi import FastAPI, UploadFile, File
from services.skills import extract_text_from_pdf, extract_skills
from services.matcher import match_resume_to_job

app = FastAPI()

@app.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):
    file_path = "uploaded_resume.pdf"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)
    resume_skills = extract_skills(text)

    job_skills = ["python", "sql", "excel"]
    match_score = match_resume_to_job(resume_skills, job_skills)

    return {
        "resume_skills": resume_skills,
        "match_score": match_score
    }

