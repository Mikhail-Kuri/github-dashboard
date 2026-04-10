import os
import json
import time
from datetime import datetime

STATE_FILE = "time_state.json"
LOG_FILE = "work_log.txt"

# ---------------------------
# 1. LOAD OLD STATE
# ---------------------------
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        data = json.load(f)
        total_time = data.get("total_time", 0)
        last_session = data.get("last_session_start", None)
else:
    total_time = 0
    last_session = time.time()

# ---------------------------
# 2. SESSION TIME
# ---------------------------
now = time.time()

if last_session:
    session_seconds = int(now - last_session)
else:
    session_seconds = 0

# ---------------------------
# 3. UPDATE TOTAL
# ---------------------------
total_time += session_seconds

# ---------------------------
# 4. SAVE NEW STATE
# ---------------------------
with open(STATE_FILE, "w") as f:
    json.dump({
        "total_time": total_time,
        "last_session_start": now
    }, f)

# ---------------------------
# 5. APPEND LOG
# ---------------------------
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(LOG_FILE, "a") as f:
    f.write(f"[{timestamp}] session={session_seconds}s | total={total_time}s\n")

# ---------------------------
# 6. GIT COMMIT
# ---------------------------
commit_message = f"update work time +{session_seconds}s (total {total_time}s)"

os.system("git add -A")
print("should have added")
os.system(f'git commit -m "{commit_message}"')

# ---------------------------
# 7. OUTPUT
# ---------------------------
print("\n🔥 TRACKING DONE")
print(f"Session: {session_seconds}s")
print(f"Total: {total_time}s")
print(f"Commit: {commit_message}")