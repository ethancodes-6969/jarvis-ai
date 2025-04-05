import datetime
import webbrowser
import random
import os
import psutil
import pyjokes
import wikipedia
import pywhatkit
import json
from pathlib import Path
from config.settings import ERROR_MESSAGES, GREETING_ALIASES

# Constants
NOTES_FILE = Path("/Users/krishsanghavi/Downloads/Storage/AVA/data/notes.json")
TODOS_FILE = Path("/Users/krishsanghavi/Downloads/Storage/AVA/data/todos.json")

# Ensure data directory exists
Path("/Users/krishsanghavi/Downloads/Storage/AVA/data").mkdir(parents=True, exist_ok=True)

def save_note(content):
    notes = []
    if NOTES_FILE.exists():
        with open(NOTES_FILE, 'r') as f:
            notes = json.load(f)
    notes.append({
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'content': content
    })
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f)

def get_todos():
    if TODOS_FILE.exists():
        with open(TODOS_FILE, 'r') as f:
            return json.load(f)
    return []

def process_command(command: str) -> str:
    command = command.lower()
    
    try:
        # Time and Date commands
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}"
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            return f"Today is {current_date}"
        
        # System commands
        elif "battery" in command:
            try:
                battery = psutil.sensors_battery()
                if battery:
                    return f"Battery is at {battery.percent}% {'and charging' if battery.power_plugged else 'and not charging'}"
                return ERROR_MESSAGES["battery_info"]
            except Exception:
                return ERROR_MESSAGES["battery_info"]
        
        elif "screenshot" in command:
            try:
                import pyautogui
                screenshot_path = f"/Users/krishsanghavi/Downloads/Storage/AVA/screenshots/screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
                pyautogui.screenshot(screenshot_path)
                return f"Screenshot saved to {screenshot_path}"
            except Exception:
                return ERROR_MESSAGES["screenshot_permission"]
        
        # Web functions
        elif "search google for" in command:
            try:
                query = command.replace("search google for", "").strip()
                webbrowser.open(f"https://www.google.com/search?q={query}")
                return f"Searching Google for {query}"
            except Exception:
                return ERROR_MESSAGES["browser_launch"]
        
        elif "search youtube for" in command:
            try:
                query = command.replace("search youtube for", "").strip()
                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
                return f"Searching YouTube for {query}"
            except Exception:
                return ERROR_MESSAGES["youtube_error"]
        
        elif "play" in command and "youtube" in command:
            try:
                song = command.replace("play", "").replace("on youtube", "").strip()
                pywhatkit.playonyt(song)
                return f"Playing {song} on YouTube"
            except Exception:
                return ERROR_MESSAGES["youtube_error"]
        
        elif "wikipedia" in command:
            try:
                query = command.replace("wikipedia", "").replace("search", "").replace("for", "").strip()
                summary = wikipedia.summary(query, sentences=2)
                return summary
            except Exception:
                return ERROR_MESSAGES["wikipedia_error"]
        
        # Personal assistant tasks
        elif "save note" in command:
            try:
                note_content = command.replace("save note", "").strip()
                save_note(note_content)
                return "Note saved successfully"
            except Exception:
                return ERROR_MESSAGES["storage_permission"]
        
        elif "read todos" in command or "read my todo list" in command:
            try:
                todos = get_todos()
                if not todos:
                    return "Your todo list is empty"
                return "Here are your todos: " + ". ".join(todos)
            except Exception:
                return ERROR_MESSAGES["file_access"]
        
        elif "motivate me" in command:
            quotes = [
                "The only way to do great work is to love what you do.",
                "Innovation distinguishes between a leader and a follower.",
                "Stay hungry, stay foolish.",
                "The future belongs to those who believe in the beauty of their dreams."
            ]
            return random.choice(quotes)
        
        # Greeting commands
        elif any(word in command for word in GREETING_ALIASES):
            greetings = ["Hello!", "Hi there!", "Hey! How can I help?"]
            return random.choice(greetings)
        
        elif "tell me a joke" in command:
            try:
                return pyjokes.get_joke()
            except Exception:
                return "I couldn't think of a joke right now."
        
        # Website commands
        elif "open youtube" in command:
            try:
                webbrowser.open("https://www.youtube.com")
                return "Opening YouTube for you"
            except Exception:
                return ERROR_MESSAGES["browser_launch"]
        
        elif "open google" in command:
            try:
                webbrowser.open("https://www.google.com")
                return "Opening Google for you"
            except Exception:
                return ERROR_MESSAGES["browser_launch"]
        
        # Default response
        return "I'm not sure how to help with that yet. (I am still being developed)"
        
    except Exception as e:
        return f"I encountered an unexpected error. Please try again."