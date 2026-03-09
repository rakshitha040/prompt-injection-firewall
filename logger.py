import json
from datetime import datetime

LOG_FILE = "logs.json"

def log_event(prompt, attack_type, status):

    log = {
        "time": str(datetime.now()),
        "prompt": prompt,
        "attack_type": attack_type,
        "status": status
    }

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(log)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)