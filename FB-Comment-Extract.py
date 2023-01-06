from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd

#read facebook links from csv
pages = pd.read_csv('basic_links.csv')
pages = pages[['Links']]
# code to ignore browser notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome('Drivers/chromedriver.exe', options=chrome_options)

# open the webpage
driver.get("https://wwww.facebook.com/")

# target username
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

# enter username and password
username.clear()
username.send_keys("natlang@proton.me")  # nlpproject3a@gmail.com
password.clear()
# use your username and password
password.send_keys("nlp12345")  # thisispassword

# target the login button and click it
time.sleep(5)
button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(10)
print("Logged in")

# program to parse comments


def Commentparse():
    driver.get(url)
    time.sleep(5)


    comments = driver.find_element(By.CLASS_NAME, "ch")
    listc = comments.find_elements(By.CLASS_NAME, "ef")

    print(len(listc))

    for i in range(0, len(listc) - 1):
        if i == 0:
            continue
        comment = listc[i].find_element(By.CSS_SELECTOR, "div>div").text
        print(comment)
        Comment.append(comment)


# Program to scrape comments from each page
Comment = []
prevcomment = []
cnt = 0
cond = True

#print(pages)

for x in range(len(pages)):

    for i in range(11):
        url = pages['Links'][x]+"&p="+str(cnt)
        print(url)

        Commentparse()

        cnt = cnt+10
    cnt = 0
#Data Cleaning

CleanComment = []
for i in range(0, len(Comment)):
    temp = Comment[i]
    templist = temp.splitlines()
    #print(templist)
    if not templist:
        continue
    CleanComment.append(templist[1])

# create a dataframe
data = pd.DataFrame({'Comment': CleanComment})
data.to_csv('Facebbok_comments26.csv')
print('data saved')
