import os
import openai
import git
import json
import requests
import random
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("Missing OpenAI API Key. Set it in .env.")

# Load configuration file
CONFIG_FILE = Path(__file__).parent / "bot_config.json"

def load_config():
    """Load bot configuration from JSON file."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "project_focus": "AI ML helper library",
        "ai_tasks": 3,
        "languages": [".py"],
        "openai_model": "gpt-3.5-turbo"
    }

config = load_config()
project_focus = config.get("project_focus", "General Project")
ai_tasks = config.get("ai_tasks", 3)
languages = config.get("languages", [".py"])
openai_model = config.get("openai_model", "gpt-3.5-turbo")

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Initialize directories
REPO_DIR = Path(__file__).parent
PROJECT_DIR = REPO_DIR / "ai_work" / project_focus.replace(" ", "_")
LOGS_DIR = REPO_DIR / "logs"
PROJECT_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# Logging function
log_filename = LOGS_DIR / f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
def log(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    with open(log_filename, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry + "\n")

log(f"🚀 AI Code Bot started working on project: {project_focus}")

# Initialize Git repository
repo = git.Repo(REPO_DIR)

# Analyze existing project files
def analyze_project():
    """Analyze the current project structure and codebase."""
    existing_files = list(PROJECT_DIR.glob("**/*.*"))
    log(f"📌 Found {len(existing_files)} existing files in project.")
    return existing_files

existing_files = analyze_project()

# Generate AI-driven tasks
def generate_tasks():
    """Generate AI tasks based on the project focus."""
    prompt = f"""
    You are an AI assistant working on {project_focus}. Generate {ai_tasks} improvement tasks for the project.
    Ensure tasks are relevant and progressively improve the system.
    Provide clear, structured tasks.
    """
    log("📌 Generating AI-driven tasks...")
    response = client.chat.completions.create(
        model=openai_model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    tasks = response.choices[0].message.content.split("\n")
    log(f"✅ Generated {len(tasks)} tasks.")
    return tasks[:ai_tasks]

tasks = generate_tasks()

# Process each task
def execute_tasks(tasks):
    """Execute each AI-generated task."""
    for idx, task in enumerate(tasks, 1):
        log(f"🔍 Processing Task {idx}/{len(tasks)}: {task}")
        task_prompt = f"""
        Implement the following task in {project_focus}:
        {task}
        Ensure clear documentation, code structure, and best practices.
        """
        response = client.chat.completions.create(
            model=openai_model,
            messages=[{"role": "user", "content": task_prompt}],
            temperature=0.8
        )
        generated_code = response.choices[0].message.content
        
        if generated_code:
            filename = PROJECT_DIR / f"task_{idx}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
            filename.write_text(generated_code, encoding="utf-8")
            log(f"✅ Created: {filename}")
        else:
            log("⚠️ AI did not return valid code for this task.")

execute_tasks(tasks)

# Commit and push changes if modifications were made
if repo.is_dirty():
    repo.git.add(A=True)
    commit_message = f"AI: {project_focus} updates - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    repo.index.commit(commit_message)
    repo.remotes.origin.push()
    log(f"📌 Changes committed and pushed to GitHub: {commit_message}")
else:
    log("✅ No changes to commit. AI did not make modifications.")

log("🚀 AI Code Bot execution completed successfully.")
