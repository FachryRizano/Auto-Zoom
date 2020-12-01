from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pyautogui as pyg
#Import selenium
chrome_driver=r"C:\Users\Asus\Desktop\auto-login\chromedriver.exe"
#chrome's webdriver location, this is an exe file
driver = webdriver.Chrome(chrome_driver)


#Load driver
driver.maximize_window()
time.sleep(2)
driver.get(r"https://myclass.apps.binus.ac.id/")
# Memasukkan username
username = driver.find_element_by_id("Username")
username.send_keys("husein.shahab")

# Memasukkan password
password = driver.find_element_by_id("Password")
password.send_keys("b!Nu$25041999")

# klik tombol submit
submit = driver.find_element_by_id("btnSubmit")
submit.click()

time.sleep(2)
date = driver.find_element_by_xpath('//*[@id="studentViconList"]/tbody/tr[3]/td[1]')
date2= driver.find_element_by_xpath('//*[@id="studentViconList"]/tbody/tr[4]/td[1]')
print(date.text)
print(date2.text)
joinButton = driver.find_element_by_xpath('//*[@id="studentViconList"]/tbody/tr[20]/td[12]/div/a')
joinButton.click()

print("Parent window title: " + driver.title)

#get current window handle
p = driver.current_window_handle

#get first child window
chwd = driver.window_handles

for w in chwd:
#switch focus to child window
    if(w!=p):
        driver.switch_to.window(w)
        break
time.sleep(5)
pyg.click(722,219)
time.sleep(5)
pyg.click(698,429)
time.sleep(5)
pyg.click(750,362)
time.sleep(5)
pyg.click(840,279)
driver.quit()

# driver.quit()