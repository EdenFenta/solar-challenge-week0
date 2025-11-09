# Solar Challenge Week 0

This repository contains my work for the 10 Academy Week 0 Solar Challenge.

# How to reporduce the enviroment

1. Clone the repository:
   git clone https://github.com/EdenFenta/solar-challenge-week0.git
2. Create a virtual enviroment on local:
   python3 -m venv venv
3. Activate it the virtual enviroment:
   source venv/bin/activate
4. Install requirements:
   pip install -r requirements.txt
5. Verify CI workflow:
   The GitHub Actions workflow ci.yml runs automatically on each push to main.
   
# Project Structure
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md
