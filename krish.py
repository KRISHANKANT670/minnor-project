import speech_recognition as sr
import pyttsx3
from datetime import datetime
import pytz

# Set the time zone to Indian Standard Time (IST)
indian_timezone = pytz.timezone('Asia/Kolkata')

# Get the current UTC time
utc_now = datetime.utcnow()

# Convert the UTC time to Indian Standard Time
indian_datetime = utc_now.replace(tzinfo=pytz.utc).astimezone(indian_timezone)

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Format the date and time as a string
formatted_date = indian_datetime.strftime("%d-%B-%Y")
formatted_datetime = indian_datetime.strftime("%H:%M:")

# Get the current day
current_day = indian_datetime.strftime("%A")

# Print the results
# print("Current Date :", formatted_date)
# print("Current Time :", formatted_datetime)
# print("Current Day:", current_day)

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        # Use Google Web Speech API to recognize speech
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except Exception as e:
        print(f"Error: {e}")
        return None

# Main program loop
while True:
    # Recognize speech
    query = recognize_speech()
    
    if query:
        # Perform actions based on recognized speech
        if "hello" in query.lower():
            speak(" Hello! How can I assist you?")
        elif "date" in query.lower():
            speak(formatted_date)
        elif "day" in query.lower():
            speak(current_day)
        elif "time" in query.lower():
            speak(formatted_datetime)
        elif "what is your name" in query.lower() or "name" in query.lower() or "your name" in query.lower() or "is your name" in query.lower():
            speak("I am your Krish.")
        elif "are you human" in query.lower() or "human" in query.lower() or "you human" in query.lower():
            speak(" No No, I am not a human. I am krish, a computer-based AI language model created by Krishankant Yadav and there team. I don't have thoughts, emotions, or a physical presence. I'm here to provide information and answer your questions to the best of my abilities based on my programming and the data I was trained on.")
        elif "how can you help me" in query.lower() or "help" in query.lower() or "help me" in query.lower():
            speak(" Certainly! I can assist you in various ways, such as answering questions on a wide range of topics, explaining complex concepts, translating languages, brainstorming ideas, editing and proofreading text, providing coding help, offering recommendations, aiding in problem-solving, and engaging in casual conversation. Whether you need information, assistance with a project, or simply someone to talk to, I'm here to help. Please feel free to ask any specific questions or let me know how I can assist you further!.")
        elif " 12 november" in query.lower() or "november" in query.lower() or "12" in query.lower() or "twelve" in query.lower():
            speak(" It's Diwali, the biggest festival of Hindu religion.")
        elif "tell me something about diwali" in query.lower() or "diwali" in query.lower():
            speak(" Diwali, also known as Deepavali, is a major Hindu festival symbolizing the triumph of light over darkness and good over evil. Celebrated with lamps, fireworks, and colorful decorations, it signifies joy, prosperity, and the unity of families and communities across India and many other parts of the world.")       
        elif "thanks" in query.lower() or "exit" in query.lower():
            speak(" Goodbye! ")
            break
        else:
            speak("I didn't understand that. Can you please repeat?")
        
        

# Release resources
recognizer.close()
