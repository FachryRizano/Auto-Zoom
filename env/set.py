import pandas as pd
import numpy as np
import schedule
from datetime import date
from selenium import webdriver
import time
import pyautogui as pyg
import numpy as np
import pandas as pd
import main
import record

schedule.every().day.at("00:00").do(record.record_schedule())

def join(xpath):
    print("Start join zoom")
    driver = main.login(False)
    joinButton = driver.find_element_by_xpath(xpath)
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
    print("DONE")


df = pd.read_csv("../schedule_record.csv",index_col=0)
df['TIME'] = df['TIME'].astype(str).str[0:5]
df['DATE'] = pd.to_datetime(df['DATE'],infer_datetime_format=True)
df['DATE'] = df['DATE'].astype(str)
df = df[['DATE','TIME','VICON']]
# print(df['DATE'])

today = date.today().strftime("%Y-%m-%d")
#time
for i,date in enumerate(df['DATE']):
    if(today == date):
        schedule.every().day.at(df['TIME'][i]).do(lambda:join(df['VICON'][i]))
    
# schedule.every().day().at(df)
while True:
    schedule.run_pending()
    time.sleep(1)