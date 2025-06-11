# AI-resume-Scanning-sql
Here’s a clean, professional `README.md` description for your **AI Resume Screener with SQL Job Matching** project — ready to upload to GitHub:

---

```markdown
# 🧠 AI Resume Screener with SQL Job Matching

This project is a smart resume screening tool built with Python, **Streamlit**, and **SQLite**. It allows users to upload their resumes in PDF format and evaluates their skill match against various job descriptions stored in a SQL database.

> 🔍 Ideal for HR professionals, recruiters, and job seekers to quickly assess skill alignment.

---

## 🚀 Features

- 📄 Upload Resume: Supports PDF upload via an intuitive Streamlit interface.
- 📊 SQL-Driven Job Database: Job roles and required skills are stored in a SQLite database.
- ✅ Skill Extraction: Parses resumes to extract relevant skills using NLP.
- 📌 Match Score Calculation: Compares resume skills with job requirements.
- 🧠 Missing Skills Feedback: Identifies which required skills are missing in the resume.
- 💡 Simple & Lightweight: Runs locally, no server required.

---

## 🗂️ Project Structure

```

resume\_screening\_ai/
│
├── app.py                          # Streamlit application entry point
├── data/
│   ├── create\_job\_db.py           # Script to create and populate job database
│   └── job\_descriptions.db        # SQLite DB storing job roles & required skills
│
├── parser/
│   ├── resume\_parser.py           # Extracts skills from uploaded resume
│   └── job\_parser.py              # Fetches job descriptions from DB
│
├── utils/
│   ├── skill\_matcher.py           # Logic for match score and missing skills
│   └── text\_cleaner.py            # (Optional) Text preprocessing functions
│
└── venv/                          # Virtual environment

````

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit**
- **SQLite**
- **pdfminer.six** – PDF parsing
- **NLTK** – Basic NLP processing

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/resume_screening_ai.git
   cd resume_screening_ai
````

2. **Create and activate virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/macOS
   venv\Scripts\activate      # For Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create the database**:

   ```bash
   python data/create_job_db.py
   ```

5. **Run the app**:

   ```bash
   streamlit run app.py
   ```

---

## 📷 Screenshot

![AI Resume Screener Screenshot](screenshot.png)

---

## 📌 To Do / Future Improvements

* Improve resume parsing accuracy using `spaCy` or advanced NER.
* Add fuzzy or semantic skill matching (e.g., `sentence-transformers`).
* Visualize results with charts or graphs.
* Export result as downloadable PDF report.
* Add multi-user login and job recommendation engine.

---

## 🧑‍💻 Author

Kalaiyarasi G
Final-year B.Tech (AI & Data Science) Student
🔗 [LinkedIn](https://www.https://www.linkedin.com/in/kalaiyarasigopal/)
🌐 [Portfolio](https://github.com/kalaiyarasi2/AI-resume-Scanning-sql)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

````

---

### ✅ Notes Before Uploading:
- Replace `yourusername`, `your-profile`, and portfolio links.
- Add a `screenshot.png` of your app UI in the repo root.
- Add a `requirements.txt` with:
  ```txt
  streamlit
  pdfminer.six
  nltk
````

Would you like a `requirements.txt` or `LICENSE` file too?
