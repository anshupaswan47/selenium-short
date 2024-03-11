from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

btn_id = 'btn-main'

def btn_click(driver):
    try:
        sleep(5)
        driver.find_element(by=By.ID,value=btn_id).click()
        print("clicked")
    except:
        pass
    

i=3
while True:
    options = Options()
    options.add_extension('urban.crx')
    options.add_extension('Adblock.crx')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    sleep(2)
    driver.get("chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/popup/index.html#/welcome-consent")
    sleep(10)
    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/button[2]").click()
    driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[2]/div/div[1]/input").click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li["+str(i)+"]").click()
    sleep(4)
    chwd = driver.window_handles
    # print(chwd)
    sleep(2)
    os.system('cls')
    driver.switch_to.window(driver.window_handles[2])
    sleep(2)
    driver.get('https://ouo.io/1lkvMo')
    
    sleep(8)
    for i in range(3):
        sleep(3)
        print("wait")
        btn_click(driver)
    
    print("Done")
    driver.quit()
      
# vpn(i)
# vpn(i)