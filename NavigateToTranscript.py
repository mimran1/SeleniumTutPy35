from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import getpass


class NavigateToTranscript(object):
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.startNavigation()
    
    def startNavigation(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://ssb.cc.binghamton.edu/banner/twbkwbis.P_WWWLogin")
        self.driver.implicitly_wait(10)
        self.loginPaige()
        self.clickStudent()
        self.clickStudentRecords()
        self.clickOnlineAcademicTranscript()
        self.selectLevel()
        currentURL = self.getCurrentURL()
        print(currentURL)
        #self.endsession()
        
    def loginPaige(self):
        #Begin - get credentials and login
        USERNAME = self.username
        PASSWORD = self.password #Get password from user input
        id = self.driver.find_element_by_id("UserID")
        passwrd = self.driver.find_element(By.NAME,"PIN")
        id.send_keys(USERNAME)
        passwrd.send_keys(PASSWORD)
        clickLogin = self.driver.find_element_by_xpath("//input[@type='submit']")
        clickLogin.click()
        #End login in
        self.driver.implicitly_wait(10)
    
    def clickStudent(self):
        #Begin - get to "Student" 
        studentTab = self.driver.find_element_by_link_text("Student")
        studentTab.click()
        #End
        self.driver.implicitly_wait(10)
     
    def clickStudentRecords(self):   
        #Begin - click "Student Records"
        studentRecords = self.driver.find_element_by_link_text("Student Records")
        studentRecords.click()
        #End
        self.driver.implicitly_wait(10)
    
    def clickOnlineAcademicTranscript(self):
        #Being - click "Online Academic Transcript"
        onlineAcademicTranscript = self.driver.find_element_by_link_text("Online Academic Transcript")
        onlineAcademicTranscript.click()
        #End
        self.driver.implicitly_wait(10)
    
   
    def selectLevel(self):
        #Begin - select Graduate then Unofficial
        transcriptLevel = self.driver.find_element_by_xpath("//select[@id='levl_id']/option[1]")
        transcriptLevel.click()
        transcriptType = self.driver.find_element_by_xpath("//select[@id='type_id']/option[1]")
        transcriptType.click()
        submit = self.driver.find_element_by_xpath("//input[@type='submit'][@value='Submit']")
        submit.click()
        #End
        self.driver.implicitly_wait(10)
    
    def getCurrentURL(self):
        return self.driver.current_url
    
    def getDriver(self):
        return self.driver
    
    def endsession(self):
        self.driver.close()

USERNAME = 'mimran1'
PASSWORD = getpass.getpass() #Get password from user input
nav = NavigateToTranscript(USERNAME,PASSWORD)
nav.getDriver().get(nav.getCurrentURL())
nav.endsession()