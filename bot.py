import os
import openai
import subprocess
import json
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("Missing OpenAI API Key. Set it in .env.")

# Load configuration
CONFIG_FILE = Path(__file__).parent / "bot_config.json"

def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "project_focus": "General_Project",
        "ai_tasks": 3,
        "openai_model": "gpt-3.5-turbo"
    }

config = load_config()
project_focus = config.get("project_focus", "General_Project")
ai_tasks = config.get("ai_tasks", 3)
openai_model = config.get("openai_model", "gpt-3.5-turbo")

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize directories
REPO_DIR = Path(__file__).parent
PROJECT_DIR = REPO_DIR / "ai_work" / project_focus.replace(" ", "_")
SRC_DIR = PROJECT_DIR / "src"
TASKS_DIR = PROJECT_DIR / "tasks"
ANALYSIS_DIR = PROJECT_DIR / "analysis"
LOGS_DIR = REPO_DIR / "logs"

for directory in [TASKS_DIR, ANALYSIS_DIR, LOGS_DIR, SRC_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Logging
def log(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOGS_DIR / f"run_{datetime.now().strftime('%Y%m%d')}.log", "a") as f:
        f.write(entry + "\n")

log(f"AI Code Bot started on project: {project_focus}")

# Project analysis
existing_files = list(SRC_DIR.glob("*.py"))
existing_code = "\n\n".join(file.read_text() for file in existing_files) if existing_files else "No existing files. This is a new project."

analysis_prompt = f"""
You are improving the '{project_focus}' project.

Existing code:
{existing_code}

Identify meaningful improvements and clearly define exactly {ai_tasks} executable Python scripts to enhance the project.

For each task, provide exactly:
filename: descriptive_name.java
code:
<python script>

Do not provide explanations or markdown formatting. Separate each task with '<--script-->'.
"""

log("Generating tasks based on current analysis...")
response = client.chat.completions.create(
    model=openai_model,
    messages=[{"role": "user", "content": analysis_prompt}],
    temperature=0.7
)

raw_tasks = response.choices[0].message.content.strip().split('<--script-->')

# Parse tasks explicitly
parsed_tasks = []
for task_block in raw_tasks:
    if "filename:" in task_block and "code:" in task_block:
        try:
            filename_part, code_part = task_block.split("code:", 1)
            filename = filename_part.replace("filename:", "").strip()
            code = code_part.strip()
            if filename.endswith('.py') and ("def" in code or "import" in code):
                parsed_tasks.append((filename, code))
        except ValueError:
            continue

log(f"Generated {len(parsed_tasks)} meaningful scripts.")

# Store, validate, execute tasks
for filename, script in parsed_tasks:
    task_path = TASKS_DIR / filename
    task_path.write_text(script, encoding="utf-8")
    log(f"Stored task: {task_path}")

    # Syntax validation
    try:
        compile(script, filename=str(task_path), mode="exec")
        result = subprocess.run(["python", str(task_path)], capture_output=True, text=True, check=True)
        log(f"Execution success {task_path}:\n{result.stdout}")
        task_path.rename(SRC_DIR / filename)
        log(f"Moved executed script to src: {SRC_DIR / filename}")
    except SyntaxError as e:
        log(f"Syntax error in {task_path}: {e}")
    except subprocess.CalledProcessError as e:
        log(f"Execution failed for {task_path}: {e.stderr}")

log("AI Code Bot run complete.")