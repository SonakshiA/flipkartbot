import sqlite3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

con = sqlite3.connect('Agatha_Christie')
cur = con.cursor()

query = 'SELECT title FROM Christie_Books where rating = (select max(rating) from Christie_Books)'

cur.execute(query)

data = cur.fetchall()

book_name = data[0][0]

# automating booking

driver = webdriver.Firefox()
wait=WebDriverWait(driver,60)

# logging onto Flipkart
phoneno = '9876543210' # sample phone no
password= 'iloveshopping' # sample password

driver.get('https://www.flipkart.com/')
element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input')
element.send_keys(phoneno)
element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input')
element.send_keys(password)
element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button')
element.click()

#time.sleep(15) # to enter OTP


element = driver.find_element_by_class_name('_3704LK')
element.send_keys(book_name) # book_name from automating.py
element.send_keys(Keys.RETURN)
driver.maximize_window()
time.sleep(5)
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'s1Q9rs')))
    element.click()

except:
    print("Error")
