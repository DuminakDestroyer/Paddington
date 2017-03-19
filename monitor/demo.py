from selenium import webdriver

driver = webdriver.Chrome("addons/chromedriver.exe")
driver.get('http://google.com')
print(driver.title)
driver.quit()