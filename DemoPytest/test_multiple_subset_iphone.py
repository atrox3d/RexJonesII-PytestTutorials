from selenium import webdriver
from selenium.webdriver.common.by import By

def test_search_lambdatest_ecommerce():
  # driver =  webdriver.Chrome()
  # driver.maximize_window()
  options = webdriver.ChromeOptions()
  options.add_argument("--headless=new")
  driver = webdriver.Chrome(options=options)

  driver.get("https://ecommerce-playground.lambdatest.io/")
  
  xpath = "//input[@placeholder='Search For Products']"
  driver.find_element(By.XPATH, xpath).send_keys("iPhone")
  
  xpath = "//button[text()='Search']"
  driver.find_element(By.XPATH, xpath).click()
  
  xpath = "//h1[contains(text(),'Search')]"
  search_value = driver.find_element(By.XPATH, xpath).text
  
  assert "iPhone" in search_value

# def test_add_to_cart():
#   result = 1
#   print("Add To Cart")
#   assert result == 3
