
import os
import requests
import subprocess

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "your-username"
REPO_NAME = "your-repository"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Scan files for TODOs and FIXMEs
def find_issues_in_file(file_path):
    issues = []
    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if "TODO" in line or "FIXME" in line:
                issues.append((file_path, i, line.strip()))
    return issues

# Get all source code files
source_files = subprocess.getoutput("git ls-files '*.py' '*.js' '*.java'").split("\n")

issues_found = []
for file in source_files:
    issues_found.extend(find_issues_in_file(file))

# Create GitHub Issues
for file, line, content in issues_found:
    issue_title = f"Issue in {file} (Line {line})"
    issue_body = f"Detected: `{content}`\n\nLocation: `{file}`, line {line}"
    
    data = {
        "title": issue_title,
        "body": issue_body,
        "labels": ["automated-issue"]
    }
    
    response = requests.post(
        f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues",
        json=data,
        headers=headers
    )

    if response.status_code == 201:
        print(f"✅ Created issue for {file} (Line {line})")
    else:
        print(f"❌ Failed to create issue: {response.json()}")

