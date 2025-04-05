from core.speech import listen, speak

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
                    speak(f"You said: {command}")
    except KeyboardInterrupt:
        speak("Manual shutdown initiated. Goodbye!")
