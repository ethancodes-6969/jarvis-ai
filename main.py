from core.speech import listen, speak
from brain.processor import process_command
from config.settings import DEFAULT_MODE, RESPONSE_DELAY, LOG_ENABLED, AVAILABLE_COMMANDS
from utils.logger import ConversationLogger
import time

class InputMode:
    VOICE = "voice"
    TEXT = "text"

def get_command(current_mode):
    if current_mode == InputMode.TEXT:
        return input("Type your command: ").strip()
    return listen()

def show_help():
    help_text = "Available Commands:\n\n"
    for category, commands in AVAILABLE_COMMANDS.items():
        help_text += f"\n{category}:\n"
        help_text += "\n".join(f"  • {cmd}" for cmd in commands)
        help_text += "\n"
    return help_text

if __name__ == "__main__":
    # Initialize with config default
    current_mode = InputMode.TEXT if DEFAULT_MODE == "text" else InputMode.VOICE
    logger = ConversationLogger() if LOG_ENABLED else None
    
    speak("Welcome Krish, I am AVA. How can I assist you?")

    try:
        while True:
            command = get_command(current_mode)
            
            if command:
                # Handle help command
                if command.lower() == "help":
                    response = show_help()
                    print(response)  # Print help text instead of speaking it
                    continue
                
                # Handle mode switching
                if "switch to text mode" in command.lower():
                    current_mode = InputMode.TEXT
                    response = "Switching to text mode"
                elif "switch to voice mode" in command.lower():
                    current_mode = InputMode.VOICE
                    response = "Switching to voice mode"
                # Handle exit commands
                elif "stop" in command.lower() or "exit" in command.lower():
                    response = "Shutting down. Goodbye!"
                    speak(response)
                    if logger:
                        logger.log_interaction(command, response)
                    break
                else:
                    # Process other commands
                    response = process_command(command)
                
                # Add natural delay
                time.sleep(RESPONSE_DELAY)
                
                # Log interaction
                if logger:
                    logger.log_interaction(command, response)
                
                speak(response)
                
    except KeyboardInterrupt:
        final_response = "Manual shutdown initiated. Goodbye!"
        speak(final_response)
        if logger:
            logger.log_interaction("KeyboardInterrupt", final_response)
