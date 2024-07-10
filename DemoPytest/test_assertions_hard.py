import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class AssertionsTest():
  pass

@pytest.fixture
def driver():
  options = webdriver.ChromeOptions()
  options.add_argument("--headless=new")
  driver = webdriver.Chrome(options=options)
  return driver

@pytest.mark.xfail(reason='testing test fail')
def test_lambdatest_radio_button_demo_value(driver):
  # driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")

  xpath = "//h4[contains(text(),'Gender')]//following::input[@value='Male']"
  driver.find_element(By.XPATH, xpath).click()

  xpath = "//h4[contains(text(),'Age')]//following::input[@value='15 - 50']"
  driver.find_element(By.XPATH, xpath).click()
  

  xpath = "//button[text()='Get values']"
  driver.find_element(By.XPATH, xpath).click()

  gender = driver.find_element(By.CSS_SELECTOR,
    ".genderbutton").text
  
  age_group = driver.find_element(By.CSS_SELECTOR,
    ".groupradiobutton").text
  
  print(gender)
  print("Gender Object: \t", id(gender))
  print("Male Object: \t", id("Male"))
  assert gender is "Male", "Gender Is Not Correct"
  #
  # testing stops here
  #
  assert driver.title.__contains__("Selenium Grid Online")
  assert "51" in age_group, "Age Group Is Not Correct"
