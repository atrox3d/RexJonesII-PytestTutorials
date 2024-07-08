import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
  options = webdriver.ChromeOptions()
  options.add_argument("--headless=new")
  driver = webdriver.Chrome(options=options)
  return driver

def test_lambdatest_simple_form_demo(driver):
  # driver = webdriver.Chrome()
  # driver.maximize_window()
  driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

  xpath = "//input[@id='user-message']"
  driver.find_element(By.XPATH, xpath).send_keys("Pytest Is A Test Framework")
  driver.find_element(By.ID, "showInput").click()
  message = driver.find_element(By.ID, "message").text
  assert message == "Pytest Is A Test Framework"
