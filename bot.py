import os
import openai
import git
import time
import json
import requests
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("Missing OpenAI API Key. Set it in .env.")

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Initialize repository and folder structure
REPO_DIR = Path(__file__).parent
AI_WORK_DIR = REPO_DIR / "ai_work"
LOGS_DIR = REPO_DIR / "logs"
CONFIG_FILE = REPO_DIR / "bot_config.json"

# Ensure directories exist
AI_WORK_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# Load configuration file
def load_config():
    """Load bot configuration from JSON file."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"languages": [".py"]}  # Default to Python if no config file

config = load_config()
languages = config.get("languages", [".py"])  # Get the list of languages to generate

# Create log file with timestamp
log_filename = LOGS_DIR / f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
def log(message):
    """Print and write logs to the log file."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    with open(log_filename, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry + "\n")

log("🚀 AI Code Bot started running...")

# Initialize Git repository
repo = git.Repo(REPO_DIR)

# ✅ Fetch a unique automation idea from a free API
def fetch_automation_idea():
    """Fetch a unique automation idea from a free API."""
    try:
        response = requests.get("https://api.publicapis.org/entries")
        if response.status_code == 200:
            data = response.json()
            entries = data.get("entries", [])
            if entries:
                api_entry = random.choice(entries)
                idea = f"Create a script that interacts with the {api_entry['API']} API ({api_entry['Description']})."
                log(f"📌 Selected Automation Idea: {idea}")
                return idea
    except Exception as e:
        log(f"⚠️ Error fetching automation idea: {e}")
    return "Create a script that generates random useful automation tools."

# ✅ Always generate a **new** script every time the bot runs
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# ✅ Loop through each language and generate a script
for lang in languages:
    ext = lang.strip().lower()
    if ext not in [".py", ".java", ".c", ".js", ".html"]:
        log(f"⚠️ Skipping unsupported language: {ext}")
        continue

    # Set directory based on language
    lang_dir = AI_WORK_DIR / ext.lstrip(".")
    lang_dir.mkdir(parents=True, exist_ok=True)

    new_file = lang_dir / f"script_{timestamp}{ext}"
    
    # Fetch an automation idea dynamically
    selected_task = fetch_automation_idea()

    code_prompt = f"""
    Write a **completely unique** script in {ext} programming language.
    The script should perform the following task:

    {selected_task}

    Requirements:
    - Use functions (if applicable) with proper documentation.
    - Be well-structured and readable.
    - Include helpful inline comments.
    - Provide full script output.

    Ensure the script follows best practices for {ext}.
    """
    
    log(f"📌 Generating a {ext} script: {new_file}")
    ai_generated_code = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": code_prompt}],
        temperature=0.9
    ).choices[0].message.content

    if ai_generated_code:
        new_file.write_text(ai_generated_code, encoding="utf-8")
        log(f"✅ New {ext} file created: {new_file}")
    else:
        log(f"⚠️ AI did not return valid {ext} code. Skipping.")

# ✅ Always modify existing files by adding new code
for lang in languages:
    lang_dir = AI_WORK_DIR / lang.lstrip(".")
    for file in lang_dir.glob(f"*.{lang.lstrip('.')}"):
        log(f"🔍 Enhancing file: {file}")

        original_code = file.read_text(encoding="utf-8")

        # Ensure AI always adds new content
        modify_prompt = f"""
        Below is an existing script. Add **new functionality** to improve it. 
        You can:
        - Add a new function.
        - Add an extra feature.
        - Extend an existing class.
        - Ensure the new code is useful, with proper comments.

        Do not just fix errors—expand functionality.

        ```{lang}
        {original_code}
        ```
        Provide the improved full script.
        """
        
        modified_code = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": modify_prompt}],
            temperature=0.9
        ).choices[0].message.content

        if modified_code and modified_code != original_code:
            file.write_text(modified_code, encoding="utf-8")
            log(f"✅ Updated file: {file}")
        else:
            log(f"⚠️ AI did not make significant changes: {file}")

# ✅ Commit and push changes if modifications were made
if repo.is_dirty():
    repo.git.add(A=True)
    commit_message = f"AI: Updated scripts with new features - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    repo.index.commit(commit_message)
    repo.remotes.origin.push()
    log(f"📌 Changes committed and pushed to GitHub: {commit_message}")
else:
    log("✅ No changes to commit. AI did not make modifications.")

log("🚀 AI Code Bot execution completed successfully.")
