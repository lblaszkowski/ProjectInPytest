from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")
driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']").click()
driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys('Dubai')
driver.find_element_by_xpath("//span[text()='Dubai']").click()
driver.find_element_by_name("checkin").send_keys("22/10/2019")
driver.find_element_by_name("checkout").send_keys("29/10/2019")
driver.find_element_by_id("travellersInput").click()
driver.find_element_by_id("adultInput").clear()
driver.find_element_by_id("adultInput").send_keys("4")
driver.find_element_by_id("childInput").clear()
driver.find_element_by_id("childInput").send_keys("4")
driver.find_element_by_xpath("//button[text()=' Search']").click()
# //h4[contains(@class,'list_title')]//b
hotels = driver.find_elements_by_xpath("//h4[contains(@class,'list_title')]//b")
hotel_name = [hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_name:
    print("Hotel name: " + name)

driver.close()
driver.quit()