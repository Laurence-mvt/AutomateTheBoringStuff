#! usr/bin/env bash
# alumniScraper.py - Scrapes LSE alumni emails from the US alumni website 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyinputplus, sys, time
import logging
import pprint

logging.basicConfig(level=logging.INFO, format=' %(asctime)s -  %(levelname)s -  %(message)s')
# logging.disable(logging.CRITICAL)

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
alumDetails = []
"""alum = {"name": 'exampleName', 
        "location": 'exampleLocation', 
        "experience": 'exampleExperience',
        "primaryEmail": 'examplePrimary',
        "secondaryEmail": 'exampleSecondary',
        "addresses": 'exampleAddresses',
        "workAddress": 'exampleWork',
        "homeAddress": 'exampleHome'}
"""
alumCardElems = []
alumNameElems = []

# get first 100 results of alumni cards
alumCardElems = alumCardElems + browser.find_elements_by_css_selector('.row.bizcard')
alumNameElems = alumNameElems + browser.find_elements_by_css_selector('.media-heading.bizcard_zoom_activator')
logging.info('length of alumCardElems: ' + str(len(alumCardElems)) + '| length of alumNameElems: ' + str(len(alumNameElems)))

emails = []
alumList = []

# get alum Ids
alumIds = []
for alum in alumCardElems:
    alumIds.append(alum.get_attribute('id'))
assert len(alumIds) == len(alumCardElems), f"alumIds ({len(alumIds)}) are not the same length as alumCardElems ({len(alumCardElems)})"

# for each .row.bizcard alumCardElem
for index, nameElem in enumerate(alumNameElems[:5]):
    logging.info(f'index: {index}')
    alum = {}
    
    # get alums Id
    alumId = str(alumIds[index])

    # reveal alum info
    nameElem.click()
    time.sleep(2)

    # Get alum name
    alum["name"] = nameElem.text

    # Get location
    # set xpath for addresses using alums Id
    locationPathX = "//*[@id='" + alumId + "']//div[@class='col-sm-10']"
    locationWithName = browser.find_element_by_xpath(locationPathX).text # contains alum name
    locationNoName = locationWithName.replace(alum["name"], "").strip()
    alum["location"] = locationNoName

    # Get addresses
    # set xpath for addresses using alums Id
    #homePathX = "//div[@id='" + alumId + "']//a[@class='btn btn-primary btn-xs']"
    addressPathX = "//*[@id='postcard_" + alumId + "']/div[2]"
    alum["addresses"] = browser.find_element_by_xpath(addressPathX).text
    

    # Get work experience
    experiencePathX = "//div[@id='" + alumId + "']//b"
    # check if have work experience, if not set to null
    try:
        alum["experience"] = browser.find_element_by_xpath(experiencePathX).text
    except:
        alum["experience"] = None
    
    # Get emails
    # check if have primary email, if not set to null    
    # set xpath for primary email using alums Id
    primaryEmailPathX = "//div[@id='" + alumId + "']//a[@class='btn btn-primary btn-xs']"
    try:
        emailElem = browser.find_element_by_xpath(primaryEmailPathX)
        alum["primaryEmail"] = emailElem.get_attribute('href')[7:]  # splice to remove the 'mailto:' at beginning of email
    except:
        alum["primaryEmail"] = None

    # check if have a secondary email, if not set to null
    # set xpath for secondary email using alums Id
    secondaryEmailPathX = "//div[@id='" + alumId + "']//a[@class='btn btn-info btn-xs']"
    try:
        secEmailElem = browser.find_element_by_xpath(secondaryEmailPathX)
        alum["secondaryEmail"] = secEmailElem.get_attribute('href')[7:] # splice to remove the 'mailto:' at beginning of email
    except:
        alum["secondaryEmail"] = None

    # Add alum to alum list 
    alumList.append(alum)


pprint.pprint(alumList)

"""# scroll down to get next 100
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END) # scroll to bottom"""
