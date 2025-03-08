import os
import openai
import git
import time
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

# Ensure directories exist
AI_WORK_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

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

# Find all Python files inside ai_work (excluding bot.py and logs)
python_files = [f for f in AI_WORK_DIR.rglob("*.py")]

# Function to generate AI-written code
def generate_code(prompt):
    """Uses OpenAI API to generate new Python code."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.9  # Higher temp for more creativity
        )
        return response.choices[0].message.content
    except Exception as e:
        log(f"❌ Error in AI generation: {e}")
        return None

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
new_file = AI_WORK_DIR / f"script_{timestamp}.py"

# Fetch an automation idea dynamically
selected_task = fetch_automation_idea()

code_prompt = f"""
Write a **completely unique** Python script.
The script should perform the following task:

{selected_task}

Requirements:
- Use functions with proper docstrings.
- Be well-structured and readable.
- Include helpful inline comments.
- Add a `main()` function for execution.

Provide the full script as output.
"""
log(f"📌 Generating a unique Python script: {new_file}")
ai_generated_code = generate_code(code_prompt)

if ai_generated_code:
    new_file.write_text(ai_generated_code, encoding="utf-8")
    log(f"✅ New Python file created: {new_file}")
    python_files.append(new_file)
else:
    log("⚠️ AI did not return valid code. Skipping new file creation.")

# ✅ Process existing files (modify and improve)
for file in python_files:
    log(f"🔍 Processing file: {file}")
    original_code = file.read_text(encoding="utf-8")

    # Generate improvements
    prompt = f"""
    Below is a Python script. Improve the code by:
    - Adding missing docstrings
    - Adding helpful inline comments
    - Ensuring function names are descriptive
    - Optimizing logic if needed
    - Keeping structure clean and readable

    ```python
    {original_code}
    ```
    Provide the improved full script as output.
    """
    improved_code = generate_code(prompt)

    if improved_code and improved_code != original_code:
        file.write_text(improved_code, encoding="utf-8")
        log(f"✅ Updated file: {file}")
    else:
        log(f"⚠️ No significant improvements made to: {file}")

# ✅ Commit and push changes if modifications were made
if repo.is_dirty():
    repo.git.add(A=True)
    commit_message = f"🤖 AI: New script + Code improvements - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    repo.index.commit(commit_message)
    repo.remotes.origin.push()
    log(f"📌 Changes committed and pushed to GitHub: {commit_message}")
else:
    log("✅ No changes to commit. AI did not make modifications.")

log("🚀 AI Code Bot execution completed successfully.")
