from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait    
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
#Import selenium
chrome_driver=r"C:\Users\Asus\Desktop\auto-login\chromedriver.exe"
#chrome's webdriver location, this is an exe file

# untuk ngehide chrome driver sehingga browser tidak kelihatan ketika running
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# driver = webdriver.Chrome(chrome_driver,chrome_options=options)

def login():
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
    return driver




