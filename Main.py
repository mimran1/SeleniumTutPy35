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
extractAdvName = ExtractAdvisorName(driver)

nav.setSuccessor(parse)
parse.setSuccessor(navToStuSch)
navToStuSch.setSuccessor(extractAdvName)

print("Time to add more stuff. Updated in windows")

nav.processRequest("")
driver.close()
endTime = time.time()-startTime
print("Execution time: ", endTime, " secs")