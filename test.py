import m_library as mlib
import pyautogui as pt
import win32gui as wing
import webbrowser as web
import subprocess, sys, pip, time, tts

import speech_recognition
sr = speech_recognition.Recognizer()

# path = "test/aa_chrome_icon.png"
# print(mlib.check_image(path,.9))
# mlib.open_app(path,.9,10,10,.1)

# website = 'https://chat.openai.com/chat'
# web.open(website)



# while True:
#     pt.sleep(2)
#     data = wing.GetWindowText (wing.GetForegroundWindow()).lower()
#     split_data = data.rsplit(' - ',1)
#     split_data.reverse()
#     print(split_data[0])
    # return split_data[0]


# while 1 :
#     print(wing.GetWindowText(wing.GetForegroundWindow()))
#     time.sleep(3)


with speech_recognition.Microphone() as source2:
    sr.adjust_for_ambient_noise(source2, duration = 1)
    tts.speak('ready')

    while 1:
        # data = stt.listen_info()
        audio2=sr.listen(source2,timeout=None,phrase_time_limit=None)
        # text_t = sr.recognize_google(audio2)
        text_t = sr.recognize_google(audio2)
        print(text_t)