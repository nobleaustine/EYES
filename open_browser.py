import subprocess
import time
import pyautogui
import speech_recognition as sr

def convert_microphone_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Listen to the microphone input
        audio_data = recognizer.listen(source)

        try:
            # Use Google Web Speech API to recognize the audio
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

def open_brave_and_search(query):
    # Open Brave browser
    subprocess.Popen(["C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"])

    # Wait for the browser to open (you might need to adjust the sleep duration)
    time.sleep(5)

    # Type the search query in the address bar
    pyautogui.write(query)
    pyautogui.press('enter')

# Example: Open Brave and search for "Python programming"
# Example: Convert microphone input to text
result_text = convert_microphone_to_text()
# Print the result
print("Converted Text:", result_text)
open_brave_and_search(result_text)
