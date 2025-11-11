OctoFit Tracker — backend

This folder contains the Django backend for OctoFit Tracker.

Virtual environment (created by the project instructions):

Create the virtual environment (if not already created):

```bash
python3 -m venv /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv
```

Activate it (optional interactive step):

```bash
source /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv/bin/activate
```

Install requirements (already provided):

```bash
/workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv/bin/pip install -r /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/requirements.txt
```

Start the Django development server (after creating migrations and a superuser):

```bash
/workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv/bin/python manage.py migrate
/workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv/bin/python manage.py runserver 0.0.0.0:8000
```

Notes:
- Follow the project instructions in the repository `.github/instructions` for further guidance.
- Do not change directories when running commands in agent mode; use absolute paths instead.
