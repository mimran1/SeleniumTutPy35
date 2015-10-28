from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Parsing():
    
    def processRequest(self,anyobject):
        start_time = time.time()
        
        driver = webdriver.Firefox()
        driver.get("file:///C:/Users/Imran/OneDrive/Documents/Projects/Python/SeleniumTutorialPy35/src/TranscriptPage.html")
        
        
        #find all the rows (i.e. all tr tags)
        #===============================================================================
        table = driver.find_element_by_class_name("datadisplaytable")
        rows = table.find_elements_by_tag_name("tr")
        print("rows found: " ,len(rows))
        print("Extraction in progress...")
        oFile = open("writeParsedData.txt","w")
        key = ""
        termDict = {}
        courseDict = {}
        finalYearOption = ""
        for val in rows:
            line = val.text
            stringLine = line#.encode("utf-8")#
            wordsInline = stringLine.split()
            if len(wordsInline)!=0:
                if wordsInline[0] == "Term:":
                    key = wordsInline[1]+wordsInline[2]
                    termDict[key] = ""
                    courseDict = {}
                if wordsInline[0] == "CS" and wordsInline[1][0] == "5":
                    courseKey = wordsInline[0]+wordsInline[1]
                    if courseKey == "CS599" or courseKey == "CS595":
                        finalYearOption = courseKey
                    courseDict[courseKey] = ""
                    for i in range(2,len(wordsInline)):
                        courseDict[courseKey] += wordsInline[i] + " "
                    if termDict:
                        termDict[key] = courseDict
         
        for key,value in termDict.items():
            print(key + ": ")
            oFile.write(key + ": \n")
            if value:
                for key2,value2 in value.items():
                    print(key2 + ": ")
                    oFile.write(key2 + ": ")
                    print(value2)
                    oFile.write(value2 + "\n")
                print() 
                oFile.write("\n")
            
        oFile.close()
        driver.close()
        print(finalYearOption)
        print("Execution time: " + str(time.time()-start_time))
        #===============================================================================

p = Parsing()
p.processRequest("")