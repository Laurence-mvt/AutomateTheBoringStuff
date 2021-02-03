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

# get alum cards, names, and other info
alumCardElems = []
alumNameElems = []

# get first 100 results of alumni cards
alumCardElems = alumCardElems + browser.find_elements_by_css_selector('.row.bizcard')
alumNameElems = alumNameElems + browser.find_elements_by_css_selector('.media-heading.bizcard_zoom_activator')


for nameElem in alumNameElems:
    nameElem.click()
    time.sleep(1)
    # get the cards name section and click to reveal more info
    #nameElem.click()


    

"""
    alumText = alum.text
    if alumText !='':
        print(alum.text)
    else:
        print('null string')    # some null strings in results"""

    #browser.find_element_by_css_selector('media-heading.bizcard_zoom_activator').click()

"""# scroll down to get next 100
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) # scroll to bottom"""

#lD2hTINqhyg\%3D > div.col-sm-10 > h4
#L5iR9bkpLAQ\%3D > div.col-sm-10 > h4





