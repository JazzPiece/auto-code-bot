# Auto Code Bot

## Overview
Auto Code Bot is an automated script generator that creates and enhances code files in multiple programming languages using OpenAI's API. It automatically commits and pushes generated or modified code to a Git repository.

## Features
- Generates new scripts based on automation ideas fetched from an API.
- Modifies existing code files to add new functionality.
- Supports multiple programming languages (configurable in `bot_config.json`).
- Automatically commits and pushes changes to GitHub.
- Logs execution details for debugging and monitoring.

## Installation
### Prerequisites
- Python 3.9 or later
- Git installed and configured
- OpenAI API key (stored in a `.env` file)
- Task Scheduler (Windows) or a cron job (Linux/macOS) for automation

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/auto-code-bot.git
   cd auto-code-bot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Configure the bot settings in `bot_config.json`.

## Usage
### Running the Bot Manually
To run the bot and generate code:
```sh
python bot.py
```

### Automating with Task Scheduler (Windows)
1. Open **Task Scheduler**.
2. Create a new task and set **Action** → `Start a Program`.
3. Program/script: `C:\path\to\python.exe`
4. Add arguments: `C:\path\to\bot.py`
5. Set **Triggers** for scheduling the task.

### Automating with Cron (Linux/macOS)
Edit the crontab:
```sh
crontab -e
```
Add a cron job to run every hour:
```sh
0 * * * * /usr/bin/python3 /path/to/bot.py
```

## Configuration
Modify `bot_config.json` to customize settings:
```json
{
    "languages": [".py", ".java", ".c", ".js", ".html"],
    "max_new_files_per_language": 1,
    "max_modified_files_per_language": 1,
    "openai_model": "gpt-3.5-turbo"
}
```

## Logging
Execution logs are stored in the `logs/` directory, with timestamps for each run.

## Troubleshooting
- **No commits on GitHub?** Ensure Git credentials are stored:
  ```sh
  git config --global credential.helper store
  ```
- **Task Scheduler runs but doesn’t generate code?** Check `task_scheduler_test.log`.
- **Check `logs/` folder for errors.**

## License
MIT License

## Contributing
Pull requests are welcome! Open an issue for bug reports or feature requests.

