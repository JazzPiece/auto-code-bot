import subprocess
import time

print(" Running AI Code Bot...")
subprocess.run(["python", "bot.py"])  # Runs bot.py

print(" AI Code Bot execution completed!")
time.sleep(2)  # Small delay before committing changes

# Optional: Run the Git commit script automatically
print(" Now running Git commit script...")
subprocess.run(["python", "commit_changes.py"])
