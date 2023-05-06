import pyttsx3
engine = pyttsx3.init()

# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# engine.setProperty('rate',200)     # setting up new voice rate || base rate = 200


def speak(data):
    engine.say(data)
    engine.runAndWait()
    engine.stop()