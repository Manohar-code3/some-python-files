import speech_recognition as sr
import pyttsx3
import pywhatkit



listener = sr.Recognizer( )
engine =pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say('i am siri what can i do for u')
    engine.say(text)
    engine.runAndWait()
     
def take_siri():
    try:
        with sr.Microphone() as source:
            print("listening.....")
            voice=listener.listen(source) 
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'siri' in command:
                command=command.replace('siri','')
                print(command)
    except:
        pass
    return command

def run_siri():
    command=take_siri()
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song) 
        pywhatkit.playonyt(song)
        
run_siri()       