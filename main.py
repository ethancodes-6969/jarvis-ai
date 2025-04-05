from core.speech import listen, speak
from brain.processor import process_command

class InputMode:
    VOICE = "voice"
    TEXT = "text"

def get_command(current_mode):
    if current_mode == InputMode.TEXT:
        return input("Type your command: ").strip()
    return listen()

if __name__ == "__main__":
    current_mode = InputMode.VOICE
    speak("Welcome Krish, I am AVA. How can I assist you?")

    try:
        while True:
            command = get_command(current_mode)
            
            if command:
                # Handle mode switching
                if "switch to text mode" in command.lower():
                    current_mode = InputMode.TEXT
                    speak("Switching to text mode")
                    continue
                    
                elif "switch to voice mode" in command.lower():
                    current_mode = InputMode.VOICE
                    speak("Switching to voice mode")
                    continue
                
                # Handle exit commands
                if "stop" in command.lower() or "exit" in command.lower():
                    speak("Shutting down. Goodbye!")
                    break
                
                # Process other commands
                response = process_command(command)
                speak(response)
                
    except KeyboardInterrupt:
        speak("Manual shutdown initiated. Goodbye!")
