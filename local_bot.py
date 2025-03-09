import os
import json
import subprocess

def run(local_config=None, main_config=None):
    # Load configuration files if not provided
    if main_config is None:
        with open('bot_config.json') as f:
            main_config = json.load(f)
    if local_config is None:
        with open('local_bot_config.json') as f:
            local_config = json.load(f)

    # Prepare output directory for local LLM generated code
    output_dir = os.path.join("ai_work", "local_llm")
    os.makedirs(output_dir, exist_ok=True)

    # Build the prompt, including file limit instructions
    prompt = main_config.get("prompt", "Implement the required feature.")
    prompt += (
        f"\n(Note: Do not exceed {main_config['max_new_files_per_language']} new files "
        f"and {main_config['max_modified_files_per_language']} modified files.)"
    )

    # Determine which local LLM engine to use (e.g., Ollama or llama.cpp)
    engine = local_config.get("engine", "")
    model = local_config.get("model", "")
    output_text = ""

    if engine.lower() == "ollama":
        # Use Ollama CLI to generate completion
        result = subprocess.run(
            ["ollama", "run", model, "-p", prompt],
            capture_output=True, text=True
        )
        output_text = result.stdout
    elif engine.lower() == "llama.cpp":
        # Use llama.cpp CLI (assuming 'llama' is a command for the model)
        result = subprocess.run(
            ["llama", "--model", model, "--prompt", prompt],
            capture_output=True, text=True
        )
        output_text = result.stdout
    else:
        raise ValueError(f"Unsupported local LLM engine: {engine}")

    # Parse the local LLM output and save files (similar to bot.py logic)
    if "### New File:" in output_text or "### Modified File:" in output_text:
        lines = output_text.splitlines()
        current_file = None
        file_buffer = []
        for line in lines:
            if line.startswith("### New File:") or line.startswith("### Modified File:"):
                # Save content of the previous file (if any)
                if current_file and file_buffer:
                    file_path = os.path.join(output_dir, current_file)
                    with open(file_path, 'w') as f:
                        f.write("\n".join(file_buffer))
                # Start a new file section
                file_buffer = []
                current_file = line.split(":", 1)[1].strip()
            else:
                # Collect code lines for the current file
                if current_file:
                    if line.strip().startswith("```"):
                        continue  # skip markdown formatting
                    file_buffer.append(line)
        # Write the last file collected, if any
        if current_file and file_buffer:
            file_path = os.path.join(output_dir, current_file)
            with open(file_path, 'w') as f:
                f.write("\n".join(file_buffer))
    else:
        # If output isn't in the multi-file format, save it to a single file
        default_file = os.path.join(output_dir, "generated_code.txt")
        with open(default_file, 'w') as f:
            f.write(output_text)

    print(f"Local LLM generated code saved to {output_dir}")
