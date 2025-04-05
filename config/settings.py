# Default settings
DEFAULT_MODE = "text"  # or "voice"
RESPONSE_DELAY = 1  # seconds
LOG_ENABLED = True

# Error messages
ERROR_MESSAGES = {
    "microphone_access": "I don't have permission to access your microphone. Please check your system settings and grant microphone access.",
    "speaker_error": "I'm having trouble with the audio output. Please check your speaker settings.",
    "screenshot_permission": "I need screen recording permission to take screenshots. Please grant access in System Preferences → Security & Privacy → Privacy → Screen Recording.",
    "file_access": "I don't have permission to access the specified file or directory.",
    "battery_info": "Unable to retrieve battery information. This feature might not be available on your device.",
    "internet_connection": "I can't connect to the internet. Please check your connection for web-related features.",
    "browser_launch": "I couldn't open the web browser. Please check if you have a default browser set.",
    "storage_permission": "I don't have permission to save files in the specified location.",
    "wikipedia_error": "Unable to fetch Wikipedia information. Please check your internet connection.",
    "youtube_error": "Cannot access YouTube. Please check your internet connection and try again."
}

# Command aliases
GREETING_ALIASES = ["hello", "hi", "hey", "yo", "what's up", "sup"]
EXIT_ALIASES = ["stop", "exit", "quit", "bye", "goodbye"]

# Available commands help
AVAILABLE_COMMANDS = {
    "Basic Commands": [
        "hello/hi/hey - Greet AVA",
        "stop/exit - Shut down AVA",
        "switch to text mode - Change to text input",
        "switch to voice mode - Change to voice input",
        "help - Show this help message"
    ],
    "System Commands": [
        "time - Get current time",
        "date - Get current date",
        "battery - Check battery status",
        "screenshot - Take a screenshot"
    ],
    "Web Commands": [
        "search google for [query] - Search Google",
        "search youtube for [query] - Search YouTube",
        "play [song] on youtube - Play music",
        "wikipedia [topic] - Get Wikipedia summary"
    ],
    "Assistant Commands": [
        "save note [content] - Save a note",
        "read todos - Check your todo list",
        "motivate me - Get a motivation quote",
        "tell me a joke - Hear a programming joke"
    ]
}