from fastapi import FastAPI, UploadFile, File
from services.skills import extract_text_from_pdf, extract_skills
from services.matcher import match_resume_to_job,meaning_match

app = FastAPI()

@app.post("/analyze-resume")
async def analyze_resume(file: UploadFile = File(...)):
    file_path = "uploaded_resume.pdf"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)
    resume_skills = extract_skills(text)

    job_skills = ["python", "sql", "excel"]
    job_description="We need a python developer with sql and excel skills "
    skill_result=match_resume_to_job(resume_skills,job_skills)
    meaning_result=meaning_match(text,job_description)

    return {
        "resume_skills": resume_skills,
        "match_skills":  skill_result["matched_skills"],
        "missing_skills":skill_result["missing_skills"],
        "skill_score":skill_result["skill_score"],
        "meaning_score":meaning_result["score"],
        "percentage":meaning_result["score"],
        "result":meaning_result["result"]

    }

