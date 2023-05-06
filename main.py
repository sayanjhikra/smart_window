# import module
# module.checker_installer()
# import pip
# pip.main(['install', '=r', 'requirements.txt'])
import tts
import speech_recognition
import pyautogui as pt
import m_library as mlib
import app_specific_program as asp
sr = speech_recognition.Recognizer()

taskbar = {"google chrome":"app_icon/chrome_icon.png","file explorer":"app_icon/file_explorer_icon.png","control panel":"app_icon/control_panel_icon.png",
"whatsapp":"app_icon/whatsapp_icon.png","vs code":"app_icon/vs_code_icon.png","task manager":"app_icon/task_manager_icon.png"}




def second_opening_process(p_info):
    # print('nnn')
    mlib.open_app("images/window_icon.png",.7,10,10,.1)
    mlib.open_app("images/search_icon.png",.7,10,10,0)

    pt.typewrite(p_info)#Message type
    pt.hotkey('enter') #key press
    pt.sleep(1)
    tts.speak("done")



with speech_recognition.Microphone() as source2:
    sr.adjust_for_ambient_noise(source2, duration = 5)
    tts.speak('ready')

    while 1:
        # data = stt.listen_info()
        audio2=sr.listen(source2,timeout=None,phrase_time_limit=None)
        text_t = sr.recognize_google(audio2)
        data = str(text_t)
        data = data.lower()

        if data != '0':
            print(data)
            m_info = data.split()          
            if asp.basic_navigation(m_info):     #basic navigation----
            
                p_info = data.split(' ', 1)[1]  
                if len(m_info) > 1 and (m_info[0]=="open"):

                    if p_info in taskbar:
                        if mlib.open_app(taskbar[p_info],.9,15,15,.1):
                            tts.speak("done")
                    elif mlib.open_website(p_info):
                            tts.speak("done")
                    else:
                        if len(mlib.get_active_window()) != 0:
                            gs = asp.app_control(mlib.get_active_window(),m_info,p_info)
                            if gs == False:
                                second_opening_process(p_info)
                        else:second_opening_process(p_info)

                elif len(m_info) > 1 and (m_info[0]=="search"):             #search--------
                    # p_info = data.split(' ', 1)[1]
                    print(p_info)
                    # mlib.open_app(chrome[m_info[0]],.7,60,20,0)
                    # pt.typewrite(p_info)#Message type
                    # pt.hotkey('enter') #key press






