import subprocess
import os
import git
from datetime import datetime

# Initialize Git repository
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
repo = git.Repo(REPO_DIR)

# Check if there are any changes
if repo.is_dirty():
    print(" Changes detected. Committing and pushing...")
    
    # Add all changes
    repo.git.add(A=True)
    
    # Generate a commit message with timestamp
    commit_message = f" AI: Automated update - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    repo.index.commit(commit_message)

    # Push to GitHub
    origin = repo.remotes.origin
    origin.push()
    
    print(f" Changes committed and pushed: {commit_message}")
else:
    print(" No changes detected. Nothing to commit.")
