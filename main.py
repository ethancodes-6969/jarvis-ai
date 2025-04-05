from core.speech import listen, speak
from brain.processor import process_command

if __name__ == "__main__":
    speak("Welcome Krish, I am AVA. How can I assist you?")

    try:
        while True:
            command = listen()
            if command:
                if "stop" in command or "exit" in command:
                    speak("Shutting down. Goodbye!")
                    break
                else:
                    response = process_command(command)
                    speak(response)
    except KeyboardInterrupt:
        speak("Manual shutdown initiated. Goodbye!")
