import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I am your AI assistant. How can I assist you today?")

def main():
    wish_me()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)

            if "wikipedia" in command:
                speak("Searching Wikipedia...")
                command = command.replace("wikipedia", "")
                result = wikipedia.summary(command, sentences=2)
                speak("According to Wikipedia, " + result)
                

            elif "open youtube" in command:
                webbrowser.open("https://www.youtube.com")

            elif "open google" in command:
                webbrowser.open("https://www.google.com")

            elif "play music" in command:
                music_dir = "path_to_your_music_folder"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif "the time" in command:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak("The current time is " + current_time)

            elif "exit" in command:
                speak("Goodbye! Have a great day!")
                break

            else:
                speak("I'm sorry, I don't understand that command.")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your audio.")
        except sr.RequestError:
            print("Sorry, there was an error with the request. Please check your internet connection.")

if __name__ == "__main__":
    main()
