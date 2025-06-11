# skill_matcher.py
def calculate_match_score(resume_skills, required_skills):
    resume_set = set(skill.strip().lower() for skill in resume_skills)
    required_set = set(skill.strip().lower() for skill in required_skills)
    if not required_set:
        return 0.0
    return len(resume_set & required_set) / len(required_set)
