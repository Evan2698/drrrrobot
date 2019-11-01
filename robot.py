from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select 
import time
import random
import requests

browser=webdriver.Chrome(executable_path=r'/home/evan/MyApps/webdriver/chromedriver_linux64/chromedriver')

room_name = "春暖花开"
room_desc = "愿你在尘世获得幸福， 我只愿面朝大海，春暖花开"
USER = "WRU"




class TimerData:
    def __init__(self, url, content):
        self.id = url
        self.content = content
    
    def getContent(self):
        return self.content

    def getURL(self):
        return self.id

class Message:
    def __init__(self, type, user, message):
        self.tt = type
        self.usr = user
        self.msg = message

    def get_user(self):
        return self.usr
    
    def get_type(self):
        return self.tt
    
    def get_msg(self):
        return self.msg

    def to_string(self):
        return self.msg + self.usr + str(self.tt)

def parse_current_talk():
    talks = browser.find_elements_by_xpath("//*[@id='talks']//*")
    if len(talks) == 0 : 
        return Message(0, "", "")
    first = talks[0]
    if first and first.text.find("logged in") > 0:
        return Message(1, "", first.find_element_by_tag_name("span").text)

    user =  first.find_element_by_xpath("//dt//div[2]//span") 
    msg =  first.find_element_by_xpath("//dd//div//p")
    if user.text and msg.text:
        return Message(2, user.text, msg.text)
    
    return Message(0, "", msg)

def fetch_timerd_item():
    result = []
    try:
        browser.get("https://timerd.me/")
        subs = browser.find_elements_by_class_name("item-content") 
        aset = subs[0].find_elements_by_xpath("//div//h1//a")
        for a in aset:
            at = TimerData(a.get_attribute("href"), a.text)
            result.append(at)
    except:
        result = []

    return result

def ask_question(msg):
    url = 'http://i.itpk.cn/api.php?question=%s'%(msg)
    ret = requests.get(url)
    if ret.status_code == 200:        
        return ret.text
    return "我就是不想回答你～～～."

def query_timerd_item(timerList):
    browser.get("https://drrr.com/")
    browser.find_element_by_id("form-name").send_keys(USER)
    browser.find_element_by_css_selector("input[value='ENTER'").click()
    #create room
    btn = browser.find_element_by_css_selector("input[value='Create Room']")
    btn.click()
    time.sleep(1)
    browser.find_element_by_id("form-user-name").send_keys(room_name)
    browser.find_element_by_id("form-room-description").send_keys(room_desc)
    browser.find_element_by_id("form-user-limit").send_keys("10")
    Select(browser.find_element_by_id("form-user-lang")).select_by_index(44)
    browser.find_element_by_id("form-user-music").click()
    browser.find_element_by_css_selector("input[type='submit']").click()
    time.sleep(1)

    tick = 0
    random.seed()
    while True:
        try:
            if tick > 220:
                tick = 0
                tt = len(timerList)
                index = random.randint(0,tt-1)
                print(index, "index")
                browser.find_element_by_class_name("form-control").send_keys(timerList[index].getContent())
                format = 'document.getElementById("url-input").value="%s"' % (timerList[index].getURL())
                browser.execute_script(format)              
                browser.find_element_by_css_selector("input[name='post']").click()
               
        except BaseException as e:
            print(e)

        try:
            onjude = parse_current_talk()
            if onjude.get_type() == 1:
                if onjude.get_msg().find(USER) == -1:
                    browser.find_element_by_class_name("form-control").send_keys("@" + onjude.get_msg() + " " + "送你一朵❀ ^_^!")
                    browser.find_element_by_css_selector("input[name='post']").click()
            elif onjude.get_type() == 2:
                if onjude.get_msg().startswith("@" + USER):
                    resp = ask_question(onjude.get_msg()[len(USER) + 1: ])
                    nMsg = "@" + onjude.get_user() + " " + resp
                    browser.find_element_by_class_name("form-control").send_keys(nMsg)
                    browser.find_element_by_css_selector("input[name='post']").click()
                else:
                    print("need not answer!")
            else:
                print("else", onjude.to_string())
        except BaseException as f:
            print(f)

        time.sleep(2)
        tick = tick + 1
        print("time is ", tick)


def main():
    timerlist = fetch_timerd_item()
    query_timerd_item(timerlist)
    browser.close()

if __name__ == "__main__":
    main()

