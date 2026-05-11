import re
def extract_text_from_pdf(file_path):
    return "Python SQL Excel FastAPI"

def extract_skills(text):
    skills = ["python", "sql", "excel", "fastapi", "docker"]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills