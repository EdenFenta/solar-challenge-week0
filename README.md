# Solar Challenge Week 0  
This repository contains my complete work for the **10 Academy Week 0 Solar Challenge**.

---

## How to Reproduce the Environment (One Window)

```bash
# 1. Clone the repo
git clone https://github.com/EdenFenta/solar-challenge-week0.git
cd solar-challenge-week0

# 2. Create & activate virtual environment
python3 -m venv venv
# Mac/Linux:
source venv/bin/activate
# Windows (PowerShell):
# venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit dashboard
streamlit run app/main.py


GitHub Actions CI:
Automated testing via .github/workflows/ci.yml
```
### Folder Structure
```bash
src/        → Core modules & reusable code  
notebooks/  → EDA, analysis & Jupyter notebooks  
tests/      → Unit tests for all scripts  
scripts/    → Helper & utility scripts  
data/       → CSV files (git-ignored)  
app/        → Streamlit interactive dashboard
```
