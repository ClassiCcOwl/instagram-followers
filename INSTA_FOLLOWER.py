from pprint import pprint
import sys
from scipy.fft import idst
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep, gmtime, strftime

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.instagram.com/accounts/login/?hl=en"
driver.get(url)
driver.maximize_window()
begining_handels = driver.window_handles
driver.switch_to.window(begining_handels[0])
if driver.current_url != url:
    driver.close()
    driver.switch_to.window(begining_handels[1])
uuss = "khavari.7878"
ppss = ""
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(uuss)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(ppss, Keys.ENTER)


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
id = ""
driver.get("https://www.instagram.com/"+id)

# driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/div').click()
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@href, '/following')]"))).click()
# driver.find_element(By.XPATH,"//a[contains(@href, '/following')]").click()
scroll_box = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"isgrP")))
# scroll_box = driver.find_element(By.CLASS_NAME , "isgrP")
os.system("CLS")
list_end = set()
# height variable
last_ht, ht = 0, 1
while last_ht != ht:
    sleep(1)
    last_ht = ht
    ht = driver.execute_script(""" 
    arguments[0].scrollTo(0, arguments[0].scrollHeight);
    return arguments[0].scrollHeight; """, scroll_box)
    list_following = driver.find_elements(By.CLASS_NAME,'_0imsa')
    for i in list_following:
        print(i.get_attribute('title'))
        # if i.get_attribute('title') not in list_end:
        #     list_end.append(i.get_attribute('title'))
        list_end.add(i.get_attribute('title'))
print("------------------------------")
# pprint(list_end)
# print(len(list_end))


my_run = strftime("%Y-%m-%d %H-%M")
folder = id if id[-1]!="." else id+"0"
file_path = os.path.dirname(os.path.abspath(__file__))
isV = os.path.join(file_path,folder)
isThere = os.path.exists(isV)
if not isThere:
    os.makedirs(isV)
    print(f'{id} was created in {file_path} ".>" ')
    with open(f'{isV}/{id}_followers_{my_run}.txt', 'w') as f:
        f.write(f'{id} has {len(list_end)} followers \n')
        for i in list_end:
            f.write(f"'{i}',\n")

else:
    with open(f'{isV}/{id}_Followers_{my_run}.txt', 'w') as f:
        f.write(f'{id} has {len(list_end)} followers \n')
        for i in list_end:
            f.write(f"'{i}',\n")

