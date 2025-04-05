import datetime
import json
from pathlib import Path

class ConversationLogger:
    def __init__(self):
        self.log_dir = Path("/Users/krishsanghavi/Downloads/Storage/AVA/logs")
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.log_dir / f"conversation_{datetime.datetime.now().strftime('%Y%m%d')}.json"
        
    def log_interaction(self, user_input: str, ava_response: str):
        log_entry = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user_input": user_input,
            "ava_response": ava_response
        }
        
        existing_logs = []
        if self.log_file.exists():
            with open(self.log_file, 'r') as f:
                existing_logs = json.load(f)
                
        existing_logs.append(log_entry)
        
        with open(self.log_file, 'w') as f:
            json.dump(existing_logs, f, indent=2)