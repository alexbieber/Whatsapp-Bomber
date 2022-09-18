from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome(executable_path=r'd:\chromedriver.exe') #Replace the path with the location of your chromedriver
driver.get('https://web.whatsapp.com/')

wait=WebDriverWait(driver,600)
contact="friends_name"    #Replace "friends_name" with the anme of your contact

message="hi"    #Replace it with your message

sleep(20)


x_searc=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/button/div[2]/span')
x_searc.click()

x_search=driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
x_search.send_keys(contact)
x_search.send_keys(Keys.ENTER)


x_text='//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_xpath=driver.find_element_by_xpath(x_text)

rep=100     #The number of time you want to repeat the message
for i in range(rep):
    input_xpath.send_keys(string,Keys.ENTER)
