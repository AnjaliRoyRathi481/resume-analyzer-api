import fitz

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_skills(text):
    skills = ["python", "sql", "excel", "fastapi", "docker",
              "machine learning", "deep learning", "pandas",
              "numpy", "tensorflow", "pytorch", "flask", "aws"]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills
    
