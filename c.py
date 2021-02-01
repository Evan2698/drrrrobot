from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select 
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import time
import random
import requests

FIREFOX = r'/home/evan/MyWorks/drrrrobot/geckodriver/geckodriver'
CHROMEDRIVER_PATH = r'/home/evan/MyApps/webdriver/chromedriver_linux64/chromedriver'


def cookieCooks():
    #options = Options()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    #options.add_argument("window-size=1400,600")
    #options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0")
    #driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)
    #profile = webdriver.FirefoxProfile(profile_directory='/home/evan/snap/firefox/common/.mozilla/firefox/y6j7nf2k.default')

    
    options = webdriver.firefox.options.Options()
    options.add_argument("-headless")
    options.add_argument("-profile")
# put the root directory your default profile path here, you can check it by opening Firefox and then pasting 'about:profiles' into the url field 
    options.add_argument("/home/evan/snap/firefox/common/.mozilla/firefox/y6j7nf2k.default")
    

    driver = webdriver.Firefox(executable_path=FIREFOX, options=options)
    #driver.implicitly_wait(5)
    #driver.maximize_window()
    driver.get("https://jx.688ing.com/")
    cookies = driver.get_cookies()
    for cookie in cookies:
        print("%s -> %s" % (cookie['name'], cookie['value']))
    driver.close()


def main():
    cookieCooks()


if __name__ == '__main__':
    main()
