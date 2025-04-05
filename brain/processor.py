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
    
    # Time and Date commands
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today is {current_date}"
    
    # System commands
    elif "battery" in command:
        battery = psutil.sensors_battery()
        if battery:
            return f"Battery is at {battery.percent}% {'and charging' if battery.power_plugged else 'and not charging'}"
        return "Unable to get battery information"
    
    elif "screenshot" in command:
        import pyautogui
        screenshot_path = f"/Users/krishsanghavi/Downloads/Storage/AVA/screenshots/screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        pyautogui.screenshot(screenshot_path)
        return f"Screenshot saved to {screenshot_path}"
    
    # Web functions
    elif "search google for" in command:
        query = command.replace("search google for", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Searching Google for {query}"
    
    elif "search youtube for" in command:
        query = command.replace("search youtube for", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return f"Searching YouTube for {query}"
    
    elif "play" in command and "youtube" in command:
        song = command.replace("play", "").replace("on youtube", "").strip()
        pywhatkit.playonyt(song)
        return f"Playing {song} on YouTube"
    
    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").replace("search", "").replace("for", "").strip()
        try:
            summary = wikipedia.summary(query, sentences=2)
            return summary
        except:
            return "Sorry, I couldn't find that on Wikipedia"
    
    # Personal assistant tasks
    elif "save note" in command:
        note_content = command.replace("save note", "").strip()
        save_note(note_content)
        return "Note saved successfully"
    
    elif "read todos" in command or "read my todo list" in command:
        todos = get_todos()
        if not todos:
            return "Your todo list is empty"
        return "Here are your todos: " + ". ".join(todos)
    
    elif "motivate me" in command:
        quotes = [
            "The only way to do great work is to love what you do.",
            "Innovation distinguishes between a leader and a follower.",
            "Stay hungry, stay foolish.",
            "The future belongs to those who believe in the beauty of their dreams."
        ]
        return random.choice(quotes)
    
    # Existing commands
    elif any(word in command for word in ["hello", "hi", "hey"]):
        greetings = ["Hello!", "Hi there!", "Hey! How can I help?"]
        return random.choice(greetings)
    
    elif "tell me a joke" in command:
        return pyjokes.get_joke()
    
    # Website commands
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube for you"
    
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google for you"
    
    # Default response
    return "I'm not sure how to help with that yet. (I am still being developed)"