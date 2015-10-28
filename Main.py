from selenium import webdriver
import getpass
from Base import *
import time

startTime = time.time()
USERNAME = 'mimran1'
PASSWORD = getpass.getpass() #Get password from user input
driver = webdriver.Firefox()
#webDriverObject = WebDriverObject()

nav = NavigateToTranscript(USERNAME,PASSWORD,driver)
parse = Parsing(driver)
navToStuSch = NavigateToStuSchedule(driver)


nav.setSuccessor(parse)
parse.setSuccessor(navToStuSch)

print("Time to add more stuff. Updated in windows.")
print("This line should only appear in winV1 branch")

nav.processRequest("")
driver.close()
endTime = time.time()-startTime