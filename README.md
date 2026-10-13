# Shivam Kachawar — Flask Portfolio

A responsive, dark editorial-style portfolio built with Flask, Jinja, vanilla JavaScript, and CSS.

## Requirements
- Python 3.10+
- Internet connection for Google Fonts (the site otherwise works without them)

## Run locally

### Linux / macOS
```bash
chmod +x run.sh
./run.sh
```

### Windows
```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000**.

## Routes
- `/` — portfolio
- `/api/profile` — profile/project/skills JSON
- `/health` — health check

## Personalize it
Open `app.py` and update:
- `PROJECTS`: add your actual GitHub repository and live demo URLs in each project's `link` field.
- `PROFILE`: email, phone, location, education, and profile details.
- `EXPERIENCE`, `SKILLS`, and `ACHIEVEMENTS`: edit as needed.

The résumé supplied for this portfolio did not include the actual URL values behind its LinkedIn, GitHub, or project links, so these are intentionally left as placeholders rather than guessed.

## Production note
`python app.py` runs Flask's development server. For production, use a WSGI server such as Gunicorn:
```bash
pip install gunicorn
gunicorn -w 2 -b 0.0.0.0:8000 app:app
```

## Deploy to Vercel
This project includes `vercel.json` and `api/index.py` as the serverless entry point for the Flask app.

1. Push this folder to a GitHub repository.
2. In Vercel, choose **Add New → Project**, import that GitHub repository, and keep the project root at the repository root.
3. Deploy. Vercel will use `vercel.json` to build the Python function and route requests to Flask.

For automatic deployments, keep the GitHub repository connected to the Vercel project. Each push to the production branch will trigger a deployment.
