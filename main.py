from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import randint
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
url = 'https://exurl.in/976RGSbH'
options = Options()
options.add_extension('Adblock.crx')
options.add_extension('urban.crx')
options.add_experimental_option("detach", True)

user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
options.add_argument(f"user-agent={user_agent}")
driver = webdriver.Chrome(options=options)
driver.get("chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/popup/index.html#/welcome-consent")

def vpn_proccess(driver):
    driver.switch_to.window(driver.window_handles[0])
    a = '/html/body/div/div/div[3]/div[2]/div/div[1]/input'
    b = '/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li[1]'
    driver.find_element(By.XPATH,value=a).click()
    driver.find_element(By.XPATH,value=b).click()
    driver.switch_to.window(driver.window_handles[1])
    start(driver)

def vpn(driver):
    driver.switch_to.window(driver.window_handles[0])
    sleep(10)
    driver.find_element(By.XPATH,value="/html/body/div/div/div[2]/div/div/div/button[2]").click()
    driver.find_element(By.XPATH,value="/html/body/div/div/div[3]/div[2]/div/div[1]/input").click()
    driver.implicitly_wait(5)
    # i=randint(1,5)
    i=1
    driver.find_element(By.XPATH,value="/html/body/div/div/div[3]/div[2]/div/div[2]/div/ul/li["+str(i)+"]").click()
    sleep(4)
    driver.switch_to.window(driver.window_handles[1])
    sleep(1)
    start(driver)
    
def start(driver):
    driver.get(url)
    driver.maximize_window()
    sleep(8)
    driver.get('https://battlechamp.in/')
    sleep(2)
    process(driver)

def clickby_id(driver,id):
    try:
        driver.find_element(By.ID, id).click()
    except:
        clickby_id(driver,id)
    
def clickby_xpath(driver,path):
    try:
        driver.find_element(By.XPATH,path).click()
    except:
        clickby_xpath(driver,path)

def process(driver):
    # verify
    clickby_id(driver,"link") 
    sleep(16)
    print("Verified")
    # human verify
    clickby_id(driver,"tp98")
    print("wait")
    sleep(4)
    print("Human Verified")
    # 1 continue
    clickby_id(driver,"btn6")
    print("1- continue")
    sleep(16)

    # wait
    clickby_id(driver,"tp98")
    print("wait")
    sleep(4)

    #  2 continue
    clickby_id(driver,"btn6")
    print("2- continue")
    sleep(20)

    clickby_xpath(driver,'//*[@id="container"]/section[2]/div/div/section/div/div/div/div/div[8]/center[3]/div/a')
    print("Over")
    sleep(3)
    vpn_proccess(driver)
    
    

vpn(driver)