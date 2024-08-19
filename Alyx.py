import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import time
from time import sleep
import pyautogui
import wolframalpha
import subprocess
import pyjokes
from time import sleep
import webbrowser as wb
import warnings
import keyboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

warnings.filterwarnings('ignore')



engine = pyttsx3.init()

def say(audio) -> None:
    engine.say(audio)
    engine.runAndWait()


def time() -> None:
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    say("the current time is")
    say(Time)
    print("The current time is ", Time)


def date() -> None:
    day: int = datetime.datetime.now().day
    month: int = datetime.datetime.now().month
    year: int = datetime.datetime.now().year
    say("the current date is")
    say(day)
    say(month)
    say(year)
    print(f"The current date is {day}/{month}/{year}")


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])    

def wishme() -> None:
    print("Welcome back sir!!")
    say("Welcome back sir!!")

    hour: int = datetime.datetime.now().hour
    if 4 <= hour < 12:
        say("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif 12 <= hour < 16:
        say("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif 16 <= hour < 24:
        say("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        say("Good Night Sir, See You Tommorrow")

    say("Alyx at your service sir, please tell me how may I help you.")
    print("Alyx at your service sir, please tell me how may I help you.")

def essex_live_feed():

    service = Service(r'C:/Users/user/OneDrive - Southend High School for Boys/Desktop/chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    say("Opening Essex Jamme Masjid Live Feed...")

    driver.get("https://www.essexmasjid.com/live")
    try:
        while True:
            if keyboard.is_pressed('q'):
                say("Closing...")
                driver.close()
                break
    finally:
        driver.quit()


def screenshot() -> None:
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\ss.png")
    img.save(img_path)



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language="en-in")
        print(text)
        
    except Exception as e:
        print(e)
        return "Try Again"

    return text

def order_mcdonalds():

    order = []

    def main():
        #Using chromedriver to open and automate everything that is happening
        service = Service(r"C:/Users/user/OneDrive - Southend High School for Boys/Desktop/chromedriver.exe")
        driver = webdriver.Chrome(service=service)

        say("Opening McDonalds...")

        driver.get("https://deliveroo.co.uk/menu/london/southend-on-sea/mcdonalds-0016-southend/?utm_medium=affiliate&utm_source=google_maps_link&fulfillment_type=DELIVERY&geohash=u10t0tbeg")
        driver.maximize_window()
        

        say("Let's start off with a milkshake.")
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/div/div/nav/div/button').click()
        driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/div/div/nav/div/div/div/section/div/ul/li[9]/span/button/p').click()
        say("Do you know what kind of milkshake you would like or do you want me to read the milkshake menu out to you?")
        know_or_find_out = takecommand()
        if "read" in know_or_find_out:
            milkshakes = ["Medium chocolate milkshake",
                        "Large Chocolate Milkshake",
                        "Medium Strawberry Milkshake",
                        "Large Strawberry Milkshake",
                        "Medium Banana Milkshake",
                        "Large Banana Milkshake",
                        "Medium Vanilla Milkshake",
                        "Large Vanilla Milkshake"
                        ]
            say(milkshakes)
            type_of_milkshake = takecommand()
            if "medium chocolate" in type_of_milkshake:
                MCMelement = driver.find_element(By.XPATH, '//*[@id="page"]/div[2]/section/div/div[2]/section/section[10]/div[2]/div/ul/li[1]/div/div/div/div[2]/span')
                MCMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Medium Chocolate Milkshake")
                except:
                    say("An error occured")
                    exit()
            elif "large chocolate" in type_of_milkshake:
                LCMelement = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[2]/div/div/div[2]/div[3]/span/button/div/span/svg')
                LCMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Large Chocolate Milkshake")
                except:
                    say("An error occurred")
                    exit()
            elif "medium strawberry" in type_of_milkshake:
                MSMelement = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[3]/div/div/div[2]/div[3]/span/button/div')
                MSMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Medium Strawberry Milkshake")
                except:
                    say("An error occurred")
                    exit()
            elif "large strawberry" in type_of_milkshake:
                LSMelement = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[4]/div/div/div[2]/div[3]/span/button/div')
                LSMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Large Strawberry Milkshake")
                except:
                    say("An error occurred")
                    exit()
            elif "medium banana" in type_of_milkshake:
                MBMelement = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[5]/div/div/div[2]/div[3]/span/button/div')
                MBMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Medium Banana Milkshake")
                except:
                    say("An error occurred")
                    exit()
            elif "large banana" in type_of_milkshake:
                LBMelement = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[6]/div/div/div[2]/div[3]/span/button/div/span/svg')
                LBMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Large Banana Milkshake")
                except:
                    say("An error occurred")
                    exit()
            elif "medium vanilla" in type_of_milkshake:
                MVMelement = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[7]/div/div/div[2]/div[3]/span/button/div/span/svg')
                MVMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Medium Vanilla Milkshake")
                except:
                    say("An error occurred")
                    exit()
            elif "large vanilla" in type_of_milkshake:
                LVMelement = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[8]/div/div/div[2]/div[3]/span/button/div')
                LVMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Large Vanilla Milkshake")
                except:
                    say("An error occurred")
                    exit()

        elif "know" in know_or_find_out:
            type_of_milkshake = takecommand()
            if "medium chocolate" in type_of_milkshake:
                KMCMelement = driver.find_element(By.XPATH, '//*[@id="page"]/div[2]/section/div/div[2]/section/section[10]/div[2]/div/ul/li[1]/div/div/div/div[2]/span')
                KMCMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Medium Chocolate Milkshake")
                except:
                    say("An error occured")
                    exit()
            elif "large chocolate" in type_of_milkshake:
                KLCMelement = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[2]/div/div/div[2]/div[3]/span/button/div/span/svg')
                KLCMelement.click()

                try:
                    say("Added to cart successfully")
                    order.append("Large Chocolate Milkshake")
                except:
                    say("An error occurred")
                    exit()
            elif "medium strawberry" in type_of_milkshake:
                KMSMelement = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[3]/div/div/div[2]/div[3]/span/button/div')
                KMSMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Medium Strawberry Milkshake")
                except:
                    say("An error occurred")
                    exit()
            elif "large strawberry" in type_of_milkshake:
                KLSMelement = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[4]/div/div/div[2]/div[3]/span/button/div')
                KLSMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Large Strawberry Milkshake")
                except:
                    say("An error occurred")
                    exit()
            elif "medium banana" in type_of_milkshake:
                KMBMelement = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[5]/div/div/div[2]/div[3]/span/button/div')
                KMBMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Medium Banana Milkshake")
                except:
                    say("An error occurred")
                    exit()
            elif "large banana" in type_of_milkshake:
                KLBMelement = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[6]/div/div/div[2]/div[3]/span/button/div/span/svg')
                KLBMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Large Banana Milkshake")
                except:
                    say("An error occurred")
                    exit()
            elif "medium vanilla" in type_of_milkshake:
                KMVMelement = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[7]/div/div/div[2]/div[3]/span/button/div/span/svg')
                KMVMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Medium Vanilla Shake")
                except:
                    say("An error occurred")
                    exit()
            elif "large vanilla" in type_of_milkshake:
                KLVMelement = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[8]/div/div/div[2]/div[3]/span/button/div')
                KLVMelement.click()
                try:
                    say("Added to cart successfully")
                    order.append("Large Vanilla Shake")
                except:
                    say("An error occurred")
                    exit()
            elif "no" in type_of_milkshake:
                say("Ok you want no milkshake")

        say("Do you want fries")

        wannafries = takecommand()

        if "yes" in wannafries:
            say("Do you want a small, medium or large fries")
            kind_of_fries = takecommand()
            if "small" in kind_of_fries:
                say("Ordering small fries...")
                try:
                    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/div/div/nav/div/button').click()
                    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/div/div/nav/div/div/div/section/div/ul/li[7]/span/button/p').click()
                    driver.find_element(By.XPATH, '//*[@id="layout-145909724"]/ul/li[3]/div/div/div[2]/div[3]/span/button').click()
                    order.append("Small fries")
                except:
                    say("An error occurred")
                    say("No available fries for your fat dhid")                
            elif "medium" in kind_of_fries:
                say("Ordering medium fries...")
                try:
                    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/div/div/nav/div/button').click()
                    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/div/div/nav/div/div/div/section/div/ul/li[7]/span/button/p').click()
                    driver.find_element(By.XPATH, '//*[@id="layout-145909724"]/ul/li[2]/div/div/div[2]/div[3]/span/button').click()
                    order.append("Medium fries")
                except:
                    say("An error occurred")
                    say("No available fries for your fat dhid")
            elif "large" in kind_of_fries:
                say("Ordering large fries...")
                try:
                    L1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/div/div/nav/div/button').click()
                    L2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/div/div/nav/div/div/div/section/div/ul/li[7]/span/button/p').click()
                    driver.find_element(By.XPATH, '//*[@id="layout-145909724"]/ul/li[1]/div/div/div[2]/div[3]/span/button').click()
                    order.append("Large fries")
                except:
                    say("An error occurred")
                    say("No available fries for your fat dhid")
        elif "no" in wannafries:
            say("Alright.")

        say(order) 

        if "Medium Chocolate Milkshake" in order:
            say("Would you like to increase the quantity of the Medium Chocolate Shake?")
            qtyMCM = takecommand()
            if "yes" or "yeah" or "of course" or "obviously" in qtyMCM:
                say("Type in to the python terminal shell how many more you want to add")
                qtyMCMTXT = input("\n")
                int(qtyMCMTXT)
                for i in range(qtyMCMTXT):
                    QMCM = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[1]/div/div/div[2]/div[3]/span[1]/button/div')
                    QMCM.click()
                    order.append("Medium Chocolate Milkshake")
                    try:
                        say("Added successfully")
                    except:
                        say("An error occurred")
                        exit()
            elif "no" or "nah" or "nope" in qtyMCM:
                say("Alrighty then...")

        elif "Large Chocolate Milkshake" in order:
            say("Would you like to increase the quantity of the Large Chocolate Milkshake?")
            qtyLCM = takecommand()
            if "yes" or "yeah" or "of course" or "obviously" in qtyLCM:
                say("Type into the python terminal shell how much more you want to add")
                qtyLCMTXT = input("\n")
                int(qtyLCMTXT)
                for i in range(qtyLCMTXT):
                    QLCM = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[2]/div/div/div[2]/div[3]/span[1]/button/div/span/svg')
                    QLCM.click()
                    order.append("Large Chocolate Milkshake")
                    try:
                        say("Added successfully")
                    except:
                        say("An error occurred")
                        exit()
            elif "no" or "nah" or "nope" in qtyLCM:
                say("Ok")

        elif "Medium Strawberry Milkshake" in order:
            say("Would you like to increase the quantity of the Medium Strawberry Milkshake?")
            qtyMSM = takecommand()
            if "yes" or "yeah" or "of course" or "obviously" in qtyMSM:
                say("Type into the python terminal shell how much more you want to add")
                qtyMSMTXT = input("\n")
                int(qtyMSMTXT)
                for i in range(qtyMSMTXT):
                    QMSM = driver.find_element(By.XPATH, '//*[@id="layout-145909772"]/ul/li[3]/div/div/div[2]/div[3]/span[1]/button/div')
                    QMSM.click()
                    order.append("Medium Strawberry Milkshake")
                    try:
                        say("Added Successfully")
                    except:
                        say("An error occurred")
                        exit()
            elif "no" or "nah" or "nope" in qtyMSM:
                say("OK")
        
        elif "Large Strawberry Milkshake" in order:
            say("Would you like to increase the quantity of the Large Strawberry Milkshake?")
            qtyLSM = takecommand()
            if "yes" or "yeah" or "of course" or "obviously" in qtyLSM:
                say("Type into the python terminal shell how much more you want to add")
                qtyLSMTXT = input("\n")
                int(qtyLSMTXT)
                for i in range(qtyLSMTXT):
                    QLSM = driver.find_element(By.XPATH, '//*[@id="layout-146133864"]/ul/li[4]/div/div/div[2]/div[3]/span[1]/button/div')
                    QLSM.click()
                    order.append("Large Strawberry Milkshake")
                    try:
                        say("Added Successfully")
                    except:
                        say("An error occurred")
                        exit()
            elif "no" or "nah" or "nope" in qtyLSM:
                say("Ok")
        
        elif "Medium Banana Milkshake" in order:
            say("Would you like to increase the quantity of the Medium Banana Milkshake?")
            qtyMBM = takecommand()
            if "yes" or "yeah" or "of course" or "obviously" in qtyMBM:
                say("Type into the python shell how much more you want to add")
                qtyMBMTXT = input("\n")
                int(qtyMBMTXT)
                for i in range(qtyMBMTXT):
                    QMBM = driver.find_element(By.XPATH, '//*[@id="layout-146133864"]/ul/li[5]/div/div/div[2]/div[3]/span[1]/button/div/span/svg')
                    QMBM.click()
                    order.append("Medium Banana Milkshake")
                    try:
                        say("Added Successfully")
                    except:
                        say("An error occurred")
                        exit()
            elif "no" or "nah" or "nope" in qtyMBM:
                say("Ok")
        
        elif "Large Banana Milkshake" in order:
            say("Would you like to increase the quantity of the Medium Banana Milkshake?")
            qtyLBM = takecommand()
            if "yes" or "yeah" or "of course" or "obviously" in qtyLBM:
                say("Type into the python; shell how much more you want to add")
                qtyLBMTXT = input("\n")
                int(qtyLBMTXT)
                for i in range(qtyLBMTXT):
                    QLBM = driver.find_element(By.XPATH, '//*[@id="layout-146133864"]/ul/li[6]/div/div/div[2]/div[3]/span[1]/button/div/span/svg')
                    QLBM.click()
                    order.append("Large Banana Milkshake")
                    try:
                        say("Added Successfully")
                    except:
                        say("An error occurred")
                        exit()
            elif "no" or "nah" or "nope" in qtyLBM:
                say("Ok")
        
        elif "Medium Vanilla Milkshake" in order:
            say("Would you like to increase the quantity of the Medium Vanilla Milkshake?")
            qtyMVM = takecommand()
            if "yes" or "yeah" or "of course" or "obviously" in qtyMVM:
                say("Type into the python shell how much more you want to add")
                qtyMVMTXT = input("\n")
                qtyMVMTXT = int(qtyMVMTXT)
                for i in range(qtyMVMTXT):
                    QMVM = driver.find_element(By.XPATH, '//*[@id="layout-146133864"]/ul/li[7]/div/div/div[2]/div[3]/span[1]/button/div/span/svg')
                    QMVM.click()
                    order.append("Medium Vanilla Milkshake")
                    try:
                        say("Added Successfully")
                    except:
                        say("An error occurred")
                        exit()
            elif "no" or "nah" or "nope" in qtyMVM:
                say("Ok")
        
        elif "Large Vanilla Milkshake" in order:
            say("Would you like to increase the quantity of teh large Vanilla Milkshake?")
            qtyLVM = takecommand()
            if "yes" or "yeah" or "of course" or "obviously" in qtyLVM:
                say("Type into the python shell how much more you want to add")
                qtyLVMTXT = input("\n")
                qtyLVMTXT = int(qtyLVMTXT)
                for i in range(qtyLVMTXT):
                    QLVM = driver.find_element(By.XPATH, '//*[@id="layout-146133864"]/ul/li[8]/div/div/div[2]/div[3]/span[1]/button/div/span/svg')
                    QLVM.click()
                    order.append("Large Vanilla Milkshake")
                    try:
                        say("Added Successfully")
                    except:
                        say("An error occurred")
                        exit()
            elif "no" or "nah" or "nope" in qtyLVM:
                say("Ok")
        
        elif "Small fries" in order:
            say("Would you like to increase the quantity of the small fries")
            qtySF = takecommand()
            if "yes" or "yeah" or "of course" or "obviously" in qtySF:
                say("Type into the python shell how much more you want to add")
                qtySFTXT = input("\n")
                for i in range(qtySFTXT):
                    QSM1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/div/div/nav/div/button')
                    QSM2 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/div/div/nav/div/div/div/section/div/ul/li[7]/span/button')

                    QSM = driver.find_element(By.XPATH, '//*[@id="layout-146133899"]/ul/li[3]/div/div/div[2]/div[3]/span[1]/button/div/span/svg')
                    QSM.click()
                    order.append("Small fries")
                    try:
                        say("Added Successfully")
                    except:
                        say("An error occurred")
                        say("No available fries for your fat dhid")
            elif "no" or "nah" or "nope" in qtySF:
                say("Ok")
        
        elif "Medium Fries" in order:
            say("Would you like to increase the quantity of the medium fries.")
            qtyMF = takecommand()
            if "yes" or "yeah" or "of course" or "obviously" in qtyMF:
                say("Type into the python shell how much more you want to add")
                qtyMFTXT = input("\n")
                for i in range(qtyMFTXT):
                    QMF = driver.find_element(By.XPATH, '//*[@id="layout-146133899"]/ul/li[2]/div/div/div[2]/div[3]/span[1]/button/div/span/svg')
                    QMF.click()
                    order.append("Medium Fries")
                    try:
                        say("Added Successfully")
                    except:
                        say("An error occurred")
                        say("No available fries for your fat dhid")
            elif "no" or "nah" or "nope" in qtyMF:
                say("Ok")
        
        elif "Large Fries" in order:
            say("Would you like to increase the quantity of the Large Fries")
            qtyLF = takecommand()
            if "yes" or "yeah" or "of course" or "obviously" in qtyLF:
                say("Type into the python shell how much more you want to add")
                qtyLFTXT = input("\n")
                for i in range(qtyLFTXT):
                    QLF = driver.find_element(By.XPATH, '//*[@id="layout-146133899"]/ul/li[1]/div/div/div[2]/div[3]/span[1]/button/div')
                    QLF.click()
                    order.append("Large Fries")
                    try:
                        say("Added Successfully")
                    except:
                        say("An error occurred")
                        say("No available fries for your fat dhid")
            elif "no" or "nah" or "nope" in qtyLF:
                say("Ok")
        
        say(order)
        say("Would you like to tip the rider")
        ridertip = takecommand()
        if "yes" in ridertip:
            say("They will spend it on drugs and alcohol, dont do that.")
        if "no" in ridertip:
            say("You are a wise person.")
        say("Would you like to checkout now") 

    main()




if __name__ == "__main__":
    wishme()
    while True:
        text = takecommand().lower()
        if "time" in text:
            time()
        elif "date" in text:(
            date())

        elif "who are you" in text:
            say("I'm JARVIS created by Moosa and I'm a desktop voice assistant.")
            print("I'm JARVIS created by Moosa and I'm a desktop voice assistant.")

        elif "how are you" in text:
            say("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in text:
            say("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "good" in text:
            say("Glad to hear that sir!!")
            print("Glad to hear that sir!!")
        
        elif "note" in text:
            say("What do you want me to note down?")
            note_text = takecommand()
            note(note_text)
            say("I have made a note of that")
    
        elif "order" in text:
            order_mcdonalds()

        elif "wikipedia" in text:
            try:
                say("How many sentences of a search should i do?")
                sentence_num = takecommand()
                say("Ok wait sir, I'm searching...")
                text = text.replace("wikipedia", "")
                result = wikipedia.summary(text, sentences=sentence_num)
                print(result)
                say(result)
            except:
                say("Can't find this page sir, please ask something else")

        elif "joke" in text:
            say(pyjokes.get_joke())
        
        elif "masjid" in text:
            essex_live_feed()

        elif "where is" in text:
            ind = text.lower().split().index("is")
            location = text.split()[ind + 1:]
            url = "https://www.google.com/maps/place/" + "".join(location)
            say("This is where " + str(location) + " is")
            wb.open(url)

        elif "calculate" in text:
            app_id = "LXEE2U-ELKP2WYHU8"
            client = wolframalpha.Client(app_id)
            ind = text.lower().split().index("calculate")
            text = text.split()[ind + 1:]
            res = client.query(" ".join(text))
            answer = next(res.results).text
            print(answer)
            say("The answer is " + answer)

        elif "who is" in text or "what is" in text or "how" in text or "when" in text or "why" in text or "where" in text:
            try:
                say("Ok wait sir, I'm searching...")
                text = text.replace("who is" or "what is" or "how" or "when" or "why" or "where", "")
                result = wikipedia.summary(text, sentences=2)
                print(result)
                say(result)
            except:
                say("Can't find this page sir, please ask something else")


        elif "open youtube" in text:
            wb.open("youtube.com")

        elif "open google" in text:
            wb.open("google.com")

        elif "open stack overflow" in text:
            wb.open("stackoverflow.com")


        elif "open chrome" in text:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif "search on chrome" in text:
            try:
                say("What should I search?")
                print("What should I search?")
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                say("Can't open now, please try again later.")
                print("Can't open now, please try again later.")


        elif "screenshot" in text:
            screenshot()
            say("I've taken screenshot, please check it")


        elif "offline" in text:
            quit()

