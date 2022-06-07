if True:
    from datetime import datetime
    from time import ctime
    import webbrowser,time
    import os
    import random
    import pyttsx3
    
def engine_speak(audio_string):
    engine = pyttsx3.init() 
    engine.say(audio_string) 
    engine.runAndWait() 
    
