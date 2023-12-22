import stt
import tts
import pyautogui as pt
import m_library as mlib


key_cmd = {"close":['alt','F4'],"minimise":['win','down'],"switch":['alt','tab'],"refresh":['f5'],"desktop":['win','d'],"maximize":['win','up'],"scroll":['space'],"":[''],}
chrome = {"facebook":"chrome_icon/fb_icon.png","grow":"chrome_icon/groww_icon.png","instagram":"chrome_icon/instagram_icon.png","youtube":"chrome_icon/youtube_icon.png",
        "search":"chrome_icon/chrome_search_icon.png","ai":"chrome_icon/openai_icon.png"}
openAi = {}


# print(pt.KEYBOARD_KEYS)  #all keybord keys---

db={"google chrome": chrome, "ai":openAi}

# print(chrome["close"])

def press_multi_key(data):
    eData = key_cmd[data]
    match len(eData) :
        case 1 :
            pt.hotkey(eData[0])
        case 2:
            pt.hotkey(eData[0],eData[1])
        case 3:
            pt.hotkey(eData[0],eData[1],eData[2]) 
    pt.sleep(.01)
    tts.speak(data)



# basic navigation
def basic_navigation(m_info):
    if len(m_info) == 1 :
        data = m_info[0]
        if data in key_cmd :
            if data == "close":
                press_multi_key(data)
                return False
            elif data == "minimise":
                press_multi_key(data)
                return False
            else:
                press_multi_key(data)
                return False
        else: 
            tts.speak("say again")
            return False
    else: return True



# open app and control
def app_control (active_app,m_info,p_info):

    if active_app in db:

        if len(m_info) > 1 and (m_info[0]=="open"):                 #open-----
            # print(p_info)
            if active_app in db :
                if p_info in db[active_app]:
                    mlib.open_app(chrome[p_info],.9,15,15,.1)
                    tts.speak("done")
            else: nKey = 0

        elif len(m_info) > 1 and (m_info[0]=="search"):             #search--------
            print(p_info)
            mlib.open_app(chrome[m_info[0]],.7,60,20,0)
            pt.typewrite(p_info)#Message type
            pt.hotkey('enter') #key press
        # else: 
        return True
    else:return False