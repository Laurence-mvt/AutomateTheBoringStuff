#! usr/bin/env bash
# alumniScraper.py - Scrapes LSE alumni emails from the US alumni website 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyinputplus, sys, time

# get email and password
userEmail = sys.argv[1]
userPass = sys.argv[2]
#userEmail = pyinputplus.inputEmail('Email: ')
#userPass = pyinputplus.inputPassword('Password: ')

# open chrome browser
browser = webdriver.Chrome()

# go to alumni site login page
browser.get('http://www.aflse.org/user.html?op=login')

# enter email
browser.find_element_by_name('email').send_keys(userEmail)

# enter password
browser.find_element_by_name('password').send_keys(userPass)

# login
browser.find_element_by_name('op').click()
time.sleep(2)

# go to alumni directory
directory = browser.find_element_by_link_text('US Alumni Directory')
directory.click()
time.sleep(2)

# filter by city
browser.find_element_by_name('filter_location_city').send_keys('New York')

# search for results
browser.find_element_by_name('submit').click()
time.sleep(2)

# get alum cards, names, and other info
alumCardElems = []
alumNameElems = []

# get first 100 results of alumni cards
alumCardElems = alumCardElems + browser.find_elements_by_css_selector('.row.bizcard')
alumNameElems = alumNameElems + browser.find_elements_by_css_selector('.media-heading.bizcard_zoom_activator')

emails = []
# get alum Ids
alumIds = []
for alum in alumCardElems:
    alumIds.append(alum.get_attribute('id'))

for index, nameElem in enumerate(alumNameElems[:5]):
    print(index)
    nameElem.click()
    time.sleep(2)
    
    # get primary email
    # set xpath using alums Id
    pathX = "//div[@id='" + alumIds[index] + "']//a[@class='btn btn-primary btn-xs']"
    try:
        emailElem = browser.find_element_by_xpath(pathX)
        emails.append(emailElem.get_attribute('href'))
    except:
        emails.append(None) 

for email in emails:
    print(email)

# for each .row.bizcard alumCardElem

# TODO: check if have primary email, if not set to null

    # TODO: if yes, add to alum record (dictionary?) and check if have a secondary email

        # TODO: if yes, add to alum record; if not set to null

#postcard_\%2FpGvQFtxvec\%3D > div:nth-child(1) > div > a

"""# scroll down to get next 100
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) # scroll to bottom"""
