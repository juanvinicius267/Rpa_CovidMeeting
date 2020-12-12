import pyautogui
import time
import webbrowser
import openpyxl

#----- url de abertura do Teams -----#
_url = "https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fmeetup-join%2F19%3Ameeting_ODI2NGZjM2UtMDU5MS00NTVmLTkyOWYtMWI1ZGIzM2YwMzQw%40thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%25223bc062e4-ac9d-4c17-b4dd-3aad637ff1ac%2522%252c%2522Oid%2522%253a%2522707154c7-96c8-4c24-9c73-6c728d9da51c%2522%257d%26anon%3Dtrue&type=meetup-join&deeplinkId=17bb0b22-1c2e-43a6-937b-6f53a6fb716c&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true&promptSuccess=true"


#----- caminho das imagens para abertura do Teams -----#

iconeBrowser = ".\Images\iconTeamsBrowser.png"
iconeJoin = ".\Images\iconJoin.png"

#----Class that find the image and return the coordinate on screen----#

def findIcon(filePath):
    if( (type(filePath) == str) and len(filePath) >= 5):
        print(filePath)
        start = pyautogui.locateCenterOnScreen(filePath)
        print(start)
        return start
        
    else:
         print("Caminho do arquivo não encontrado!")

#----Function to double click on objects
         
def goToObject(position,repeat):
    i = 0
    pyautogui.moveTo(position)
    time.sleep(2)    
    while i < repeat:
        pyautogui.click()
        i+= 1
#--- Main Program ---#
webbrowser.open(_url)
time.sleep(20)
goToObject(findIcon(iconeBrowser),2)
time.sleep(5)
goToObject(findIcon(iconeJoin),1)
time.sleep(5)
