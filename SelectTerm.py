from selenium import webdriver

#-------------------------------------------------- driver = webdriver.Firefox()
# driver.get("file:///home/mohammad/Documents/Projects/Python/SeleniumTutorialPy35/src/imran2.html")

str1 = "Spring2015"

save = -1
for i in range(len(str1)):
    if str1[i] == '2':
        save = i
        break
length = save
temp = " ".join(str1[i:i+length] for i in range(0,len(str1),length))
print (temp)
# options = driver.find_element_by_xpath("//*[contains(text(),'" + str1 + "')]")
#--------------------------------------------------------------- options.click()
# submit = driver.find_element_by_xpath("//input[@type='submit'][@value='Submit']")
#---------------------------------------------------------------- submit.click()
#----------------------------------------------------------- print(options.text)


