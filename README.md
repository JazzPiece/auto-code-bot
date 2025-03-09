# auto-code-botAuto Code Bot

Overview

Auto Code Bot is an automated script generator that creates and enhances code files in multiple programming languages using OpenAI's API. It automatically commits and pushes generated or modified code to a Git repository.

Features

Generates new scripts based on automation ideas fetched from an API.

Modifies existing code files to add new functionality.

Supports multiple programming languages (configurable in bot_config.json).

Automatically commits and pushes changes to GitHub.

Logs execution details for debugging and monitoring.

Installation

Prerequisites

Python 3.9 or later

Git installed and configured

OpenAI API key (stored in a .env file)

Task Scheduler (Windows) or a cron job (Linux/macOS) for automation

Setup

Clone the repository:

git clone https://github.com/yourusername/auto-code-bot.git
cd auto-code-bot

Install dependencies:

pip install -r requirements.txt

Create a .env file and add your OpenAI API key:

OPENAI_API_KEY=your_api_key_here

Configure the bot settings in bot_config.json.

Usage

Running the Bot Manually

To run the bot and generate code:

python bot.py

Automating with Task Scheduler (Windows)

Open Task Scheduler.

Create a new task and set Action → Start a Program.

Program/script: C:\path\to\python.exe

Add arguments: C:\path\to\bot.py

Set Triggers for scheduling the task.

Automating with Cron (Linux/macOS)

Edit the crontab:

crontab -e

Add a cron job to run every hour:

0 * * * * /usr/bin/python3 /path/to/bot.py

Configuration

Modify bot_config.json to customize settings:

{
    "languages": [".py", ".java", ".c", ".js", ".html"],
    "max_new_files_per_language": 1,
    "max_modified_files_per_language": 1,
    "openai_model": "gpt-3.5-turbo"
}

Logging

Execution logs are stored in the logs/ directory, with timestamps for each run.

Troubleshooting

No commits on GitHub? Ensure Git credentials are stored:

git config --global credential.helper store

Task Scheduler runs but doesn’t generate code? Check task_scheduler_test.log.

Check logs/ folder for errors.

License

MIT License

Contributing

Pull requests are welcome! Open an issue for bug reports or feature requests.
