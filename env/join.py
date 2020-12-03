from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait    
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pyautogui as pyg
import numpy as np
import pandas as pd

def join_zoom(){
    joinButton = driver.find_element_by_xpath('//*[@id="studentViconList"]/tbody/tr[6]/td[12]/div/a')
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
}