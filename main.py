import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import random
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/accounts/login/?next=%2Fp%2FCik64zCJ61d%2F&source=desktop_nav')
driver.implicitly_wait(5)

def check_exists_by(locator, descriptor):
    if locator == 'xpath':
        try:
            driver.find_element(By.XPATH, descriptor)
        except NoSuchElementException:
            return False
        return True

    elif locator == 'cssselector':
        try:
            driver.find_element(By.CSS_SELECTOR, descriptor)
        except NoSuchElementException:
            return False
        return True


def check_entry(descriptor):
    try:
        entry.find_element(By.XPATH, descriptor)
    except NoSuchElementException:
        return False
    return True

cookies = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
cookies.click()
time.sleep(2.4)


username = driver.find_element(By.XPATH,
                               '//*[@id="loginForm"]/div/div[1]/div/label/input')
password = driver.find_element(By.XPATH,
                               '//*[@id="loginForm"]/div/div[2]/div/label/input')
login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')


#TODO: fill in password and username
username.send_keys('____')
password.send_keys('____')
login.click()


WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')))
time.sleep(2)
pw_saving = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')

pw_saving.click()

#element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div/div[1]/div[2]")))
time.sleep(15)

# Get post that you want here
driver.get('https://www.instagram.com/p/CyJMjXMsrgB/')

while check_exists_by("cssselector", '[aria-label="Weitere Kommentare laden"]'):
    more_comments = driver.find_element(By.CSS_SELECTOR, '[aria-label="Weitere Kommentare laden"]')
    more_comments.click()
    # time.sleep(2)

entries = []

list = driver.find_elements(By.CLASS_NAME, "_a9ym")
for entry in list:
    entries.append(entry.text)

# This is the xpath of the entire comment: //*[@id="mount_0_0_vu"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div[2]/div/div/ul/ul[13]
# This is the xpath of just the name in the comment: /div/li/div/div[1]/div[2]/h3/div/div/span/a
print(entries)
chosen_winner = random.randint(0, len(entries))

print("WINNER FOR GIVEAWAY:" + str(entries[chosen_winner]))

# print(list)
# driver.close()
