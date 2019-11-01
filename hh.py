from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select 
import time
import random
import requests


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

browser=webdriver.Chrome(executable_path=r'/home/evan/MyApps/webdriver/chromedriver_linux64/chromedriver')   
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


print(parse_current_talk().to_string())
browser.close()




