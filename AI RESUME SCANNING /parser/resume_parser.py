# resume_parser.py
import spacy
from io import BytesIO
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")

def extract_resume_data(file_bytes):
    text = extract_text(BytesIO(file_bytes))
    doc = nlp(text)
    skills = []
    for ent in doc.ents:
        if ent.label_ in ['SKILL', 'WORK_OF_ART', 'ORG', 'PERSON']:
            skills.append(ent.text.lower())
    return list(set(skills))
