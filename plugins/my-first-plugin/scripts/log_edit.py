import os
from datetime import datetime

# Jis project mein Claude kaam kar raha hai, us ka folder
folder = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
path = os.path.join(folder, "hook-log.txt")

with open(path, "a", encoding="utf-8") as f:
    f.write(f"Claude ne file edit ki: {datetime.now()}\n")