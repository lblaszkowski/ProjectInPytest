from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")
driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']").click()
driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys('Dubai')
driver.find_element_by_xpath("//span[text()='Dubai']").click()
# driver.find_element_by_name("checkin").send_keys("22/10/2019")
# driver.find_element_by_name("checkout").send_keys("29/10/2019")
driver.find_element_by_name("checkin").click()
# driver.find_element_by_xpath("//td[@class='day ' and text()='23']").click()
driver.find_element_by_xpath("//td[@class='day  active' and text()='24']").click()
# print(len(driver.find_elements_by_xpath("//td[@class='day ' and text()='29']")))
# driver.find_element_by_xpath("//td[@class='day ' and text()='29']")
elementy = driver.find_elements_by_xpath("//td[@class='day ' and text()='29']")
for element in elementy:
    if element.is_displayed():
        element.click()
        break


driver.close()
driver.quit()