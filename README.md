# Academic Risk Predictor

A simple hackathon project to predict academic risk using a web interface and a lightweight machine learning model.

## Project Structure

```
academic-risk-predictor/
│
├── app.py
├── ml_model.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

## Setup

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

2. Activate the environment:

   - Windows PowerShell:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```

   - Git Bash / bash:
     ```bash
     source .venv/Scripts/activate
     ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Notes

- `ml_model.py` contains placeholder prediction logic. Replace it with a real trained model for improved accuracy.
- `templates/index.html` and `static/` files provide the front-end interface.
