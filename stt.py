# import speech_recognition as sr
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
# Microphone(device_index=2)

import speech_recognition
# import tts


def listen_info():
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source2:
        # print("silence please")
        sr.adjust_for_ambient_noise(source2, duration = 0.5)
        # print("Ask Something....")
        # tts.speak("Ask Something")
        audio2=sr.listen(source2)

        text_t = sr.recognize_google(audio2)
        textt = str(text_t)
        textt = textt.lower()

        # print(type(textt))
        # print("Did you say :- "+textt)
        # tts.speak(textt)
        return textt
# listen_info(3)