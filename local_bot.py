import os
import subprocess
import json
from pathlib import Path
from datetime import datetime

# Load configuration files
CONFIG_FILE = Path(__file__).parent / "bot_config.json"
LOCAL_CONFIG_FILE = Path(__file__).parent / "local_config.json"


def load_config(config_path):
    """Load configuration from JSON file."""
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def log(message):
    """Log messages to a file."""
    logs_dir = Path(__file__).parent / "logs"
    logs_dir.mkdir(exist_ok=True)
    log_filename = logs_dir / f"local_bot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    with open(log_filename, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry + "\n")


def run_local_llm(prompt, model_path, temperature=0.7):
    """Run a local LLM inference using a command-line tool like llama.cpp or GPT4All."""
    try:
        command = [
            "llama.cpp",  # Change this to the actual local LLM binary
            "--model", model_path,
            "--prompt", prompt,
            "--temperature", str(temperature),
        ]
        
        log(f"Running local LLM with command: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        return result.stdout.strip()
    except Exception as e:
        log(f"Error running local LLM: {e}")
        return None


def main():
    """Main function to run local LLM-based automation."""
    config = load_config(CONFIG_FILE)
    local_config = load_config(LOCAL_CONFIG_FILE)
    
    model_path = local_config.get("local_llm_model", "models/llm.bin")
    prompt = "Generate a useful Python automation script."
    
    log("Starting Local AI Bot...")
    generated_code = run_local_llm(prompt, model_path)
    
    if generated_code:
        output_dir = Path(__file__).parent / "local_llm_outputs"
        output_dir.mkdir(exist_ok=True)
        
        output_file = output_dir / f"generated_script_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
        output_file.write_text(generated_code, encoding="utf-8")
        log(f"✅ Code generated and saved: {output_file}")
    else:
        log("⚠️ Failed to generate code from local LLM.")
    

if __name__ == "__main__":
    main()
