from sentence_transformers import SentenceTransformer, util
import numpy as np

smart_reader = SentenceTransformer('all-MiniLM-L6-v2')


def match_resume_to_job(resume_skills, job_skills):
    matched = set(resume_skills).intersection(set(job_skills))
    score = (len(matched) / len(job_skills)) * 100
    return {
        "matched_skills": list(matched),
        "missing_skills": list(set(job_skills) - set(resume_skills)),
        "skill_score":    round(score, 2)
    }


def meaning_match(resume_text, job_description):
    resume_numbers = smart_reader.encode(resume_text)
    job_numbers    = smart_reader.encode(job_description)
    similarity     = float(util.cos_sim(resume_numbers, job_numbers))
    percentage     = round(similarity * 100, 2)

    if percentage >= 75:
        label = "Strong Match"
    elif percentage >= 50:
        label = "Partial Match"
    else:
        label = "Weak Match"

    return {
        "score":      similarity,
        "percentage": percentage,
        "result":     label
    }


def analyse(resume_skills, job_skills, resume_text, job_description):
    skill_result   = match_resume_to_job(resume_skills, job_skills)
    meaning_result = meaning_match(resume_text, job_description)
    return {**skill_result, **meaning_result}


   