import requests
from bs4 import BeautifulSoup
import csv
from secret import username,password
from selenium import  webdriver
import time


driver=webdriver.Chrome('C:/Users/Aina Tehreem/PycharmProjects/pythonProject/venv/chromedriver')
driver.get("https://m.facebook.com")
time.sleep(2)
def login(url):
    driver.get(url)
    time.sleep(2)
    email_field = driver.find_element_by_id("m_login_email")
    password_field = driver.find_element_by_id("m_login_password")
    login_btn = driver.find_element_by_css_selector('button[data-sigil="touchable login_button_block m_login_button"] ')
    email_field.send_keys(username)
    password_field.send_keys(password)
    login_btn.click()
    time.sleep(3)
    not_now=driver.find_element_by_css_selector(' button[data-sigil="touchable"]')
    not_now.click()

login('https://m.facebook.com')

post_url= 'https://m.facebook.com/DeveloperStudentClubDHASuffaUniversity/photos/a.1451042185216529/2839108256409908/'
driver.get(post_url)
time.sleep(2)
like_button = driver.find_element_by_xpath('//*[@id="u_0_10"]')
like_button.click()

para=" And sit at all the tables, cause Jesus eats with everyone, And dance to the music, if you can't sing its native tongue, And cry for the wombs, the mothers and the empty arms,And hold high the warriors fighting now for freedoms song,"
x=para.split(',')
for i in x:
    comment = driver.find_element_by_xpath('//*[@id="composerInput"]')
    comment.send_keys(i)
    time.sleep(1)
    post_button=driver.find_element_by_css_selector('button[data-sigil="touchable composer-submit"]')
    post_button.click()
    time.sleep(2)

share_button = driver.find_element_by_xpath('//*[@id="MPhotoLowerContent"]/div/footer/div/div/div[3]/a')
share_button.click()
share_now = driver.find_element_by_xpath('//*[@id="share-with-message-button"]')
share_now.click()
time.sleep(2)
caption = driver.find_element_by_id('share_msg_input')
caption.send_keys("This post was shared using a bot that I learnt to create from Python Bootcamp 2020 held by DSC@DSU. #DSCDSU #DeveloperStudentClubs #DSCPakistan #Python #Bot")
caption_post=driver.find_element_by_css_selector('button[data-sigil="share-post-btn"]')
caption_post.click()