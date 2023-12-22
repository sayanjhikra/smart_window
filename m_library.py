import time
import pyperclip
import speech_recognition
import pyautogui as pt
import win32gui as wing
import webbrowser as web



#copy to clipbord
def copy_clipboard():
    pt.hotkey('ctrl', 'c') 
    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()

#Get message
def get_message():
    global x, y

    posiction = pt.locateOnScreen("whatsapp/smily_paperclip.png",confidence=.6)
    x = posiction[0]
    y = posiction[1]
    pt.moveTo(x, y, duration=.1)
    pt.moveTo(x+30, y-50, duration=.1)
    pt.tripleClick()
    pt.sleep(.5)
    var = copy_clipboard()
    print(var)
    return var

#Posts
def post_reponce(message):
    global x, y

    posiction = pt.locateOnScreen("whatsapp/smily_paperclip.png",confidence=.6)
    x = posiction[0]
    y = posiction[1]
    pt.moveTo(x, y, duration=.1)
    pt.moveTo(x+120, y+15, duration=.1)
    pt.click()
    pt.typewrite(message,interval=.1)#Message type
    pt.hotkey('enter') #key press
    # pt.hotkey(get_message()) #type 
    open_app("whatsapp/close.png")


#go to location
def go_to_location(path,accu,h,v):
    # "'path' is for full image path"
    # "'accu' for accuracy"
    # "'h' h for horizontal movement of cursor"
    # "'v' h for vartical movement of cursor"
    global x, y
    pt.sleep(1)
    posiction = pt.locateOnScreen(path,confidence=accu)
    if posiction is not None:
        x = posiction[0]
        y = posiction[1]

        pt.moveTo(x+h, y+v, duration=.3)
        return True
    else:
        return False
    

#open app
def open_app(path,accu,h,v,delay):
    # "'path' is for full image path"
    # "'accu' for accuracy"
    # "'h' h for horizontal movement of cursor"
    # "'v' h for vartical movement of cursor"
    # ""
    global x, y
    posiction = pt.locateOnScreen(path,confidence=accu)
    if posiction is not None:
        x = posiction[0]
        y = posiction[1]

        pt.moveTo(x+h, y+v, duration=0)
        pt.click()
        pt.sleep(delay)
        return True
    else:
        return False

#check image
def check_image(path,accu):
        posiction = pt.locateOnScreen(path,confidence=accu)
        if posiction is not None:
            return True
        else: return False

#find active window name
def get_active_window():
    data = wing.GetWindowText (wing.GetForegroundWindow()).lower()
    split_data = data.rsplit(' - ',1)
    split_data.reverse()
    return split_data[0]

#find active window name
def get_active_chrome_tab():
    data = wing.GetWindowText (wing.GetForegroundWindow()).lower()
    split_data = data.rsplit(' - ',2)   
    split_data.reverse()
    return split_data[1]


websites = {"ai":'chat.openai.com/chat',"trading view":"tradingview.com/chart","youtube":"youtube.com",'figma':'figma.com'}

# open website
def open_website(p_info):
    if p_info in websites:
        website = 'https://'+ websites[p_info]
        web.open(website)
        return True
    else:return False
# time.sleep(2)
# print()