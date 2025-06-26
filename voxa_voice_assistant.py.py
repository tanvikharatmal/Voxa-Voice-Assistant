import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
     if "open google" in c.lower():
          webbrowser.open("https://google.com")
     elif "open Facebook" in c.lower():
          webbrowser.open("https://facebook.com")
     elif "open youtube" in c.lower():
          webbrowser.open("https://youtube.com")
     elif "open linkedin" in c.lower():
          webbrowser.open("https://linkedin.com")    

if __name__ == "__main__" :
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake word "Jarvis"
        # Obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        try:
                with sr.Microphone() as source:
                     print("Listening")
                     audio = r.listen(source,timeout=3, phrase_time_limit=2)
                     word = r.recognize_google(audio)
                     if(word.lower()== "jarvis"):
                          speak("Ya")                     
                
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...") 
                    audio = r.listen(source) 
                    command = r.recognize_google(audio) 
                    print(command)

                processcommand(command)

        except Exception as e:
             print("Error; {0}". format(e))


                
