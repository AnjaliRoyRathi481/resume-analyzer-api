from pydantic import BaseModel
from typing import List

class ResumeInput(BaseModel):
    resume_text: str
    job_description: str
class AnalysisResult(BaseModel):
    resume_skills:List[str]
    matched_skills:List[str]
    missing_skills:List[str]
    skill_score:float
    meaning_score:float
    percentage:float
    result:str
