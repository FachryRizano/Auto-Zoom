from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait    
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pyautogui as pyg
import numpy as np
import pandas as pd
import main

def record_schedule():
    container=[]
    driver = main.login(True)
    # mengambil table data di web
    table = WebDriverWait(driver, 8).until(lambda driver: driver.find_elements_by_css_selector("#studentViconList tr td"))
    for tr in table:
        if(tr.text!=''):
            container.append(tr.text)
    rows = len(driver.find_elements_by_xpath('//*[@id="studentViconList"]/tbody/tr'))
    header = driver.find_element_by_xpath('//*[@id="studentViconList"]/thead/tr')
    matrix = np.array(container).reshape((rows-2),12)
    for i in range(0,(rows-2)):
        matrix[i][11] = '//*[@id="studentViconList"]/tbody/tr['+ str((i+3)) +']/td[12]/div/a'
    df = pd.DataFrame(data=matrix,columns=['DATE','TIME','CLASS','ROOM','CAMPUS','DELIVERY MODE','COURSE','WEEK','SESSION','MEETING ID','MEETING PASSWORD','VICON'])
    df.to_csv(r'C:\Users\Asus\Desktop\auto-login\schedule_record.csv')
    print("record has done")

record_schedule()


