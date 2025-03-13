import os
import openai
import subprocess

# Load OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Get changed files in latest commit
changed_files = subprocess.getoutput("git diff --name-only HEAD^ HEAD").split("\n")

review_comments = []

for file in changed_files:
    if file.endswith(".py") or file.endswith(".js") or file.endswith(".java"):  # Customize for your project
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()

        review_prompt = f"""
        Review the following code for best practices, security issues, and optimizations:
        ```python
        {code}
        ```
        Provide constructive feedback in bullet points.
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": review_prompt}],
            temperature=0.5
        )

        review_comments.append(f"### Review for {file}:\n{response.choices[0].message.content}\n\n")

# Save AI Review output
with open(".github/review_output.txt", "w", encoding="utf-8") as review_file:
    review_file.write("\n".join(review_comments))
