import json, time, os
LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "logs.json")

def log(action, filename=None, status="OK", extra=None):
    extra = extra or {}
    entry = {
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "action": action,
        "file": filename,
        "status": status,
        **extra
    }

    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w") as f:
            json.dump({"logs": [entry]}, f, indent=2)
    else:
        with open(LOG_PATH, "r") as f:
            data = json.load(f)
        data.setdefault("logs", []).append(entry)
        with open(LOG_PATH, "w") as f:
            json.dump(data, f, indent=2)
