import sys
import json
import os

STATE_FILE = "time_state.json"

# ---------------------------
# 1. GET $SECONDS
# ---------------------------
if len(sys.argv) < 2:
    print("❌ Usage: python time_commit.py $SECONDS")
    exit()

session_seconds = int(sys.argv[1])

# ---------------------------
# 2. LOAD STATE
# ---------------------------
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        data = json.load(f)
        total_time = data.get("total_time", 0)
else:
    total_time = 0

# ---------------------------
# 3. UPDATE TOTAL
# ---------------------------
total_time += session_seconds

# ---------------------------
# 4. SAVE STATE
# ---------------------------
with open(STATE_FILE, "w") as f:
    json.dump({
        "total_time": total_time
    }, f)

# ---------------------------
# 5. GIT ADD + COMMIT
# ---------------------------
commit_message = f"work session +{session_seconds}s (total {total_time}s)"

os.system("git add -A")
os.system(f'git commit -m "{commit_message}"')

# ---------------------------
# 6. OUTPUT
# ---------------------------
print("\n🔥 SESSION SAVED + COMMITTED")
print(f"Session: {session_seconds}s")
print(f"Total: {total_time}s")
print(f"Commit: {commit_message}")