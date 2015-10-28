from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

start_time = time.time()

driver = webdriver.Firefox()
driver.get("file:///C:/Users/Imran/OneDrive/Documents/Projects/Python/SeleniumTutorialPy35/src/imran3.html")

table = driver.find_element_by_xpath("//*[contains(text(),'Termination Project')]/following-sibling::*")
terminationProject = table.text
terminationProjectList = terminationProject.split("\n")
assignedInstructor = ""
for line in terminationProjectList:
    if line.startswith("Assigned"):
        assignedInstructor = line.split(": ") #assumes that there is a space after the :. If no space then split(": ") should be replaced by split(":")
        break

print(assignedInstructor[-1])

driver.close()
print("Execution time: " + str(time.time()-start_time))