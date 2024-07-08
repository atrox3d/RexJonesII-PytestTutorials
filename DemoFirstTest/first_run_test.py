import pytest
from selenium import webdriver

@pytest.fixture
def driver():
  options = webdriver.ChromeOptions()
  options.add_argument("--headless=new")
  driver = webdriver.Chrome(options=options)
  return driver

def test_lambdatest_playground(driver):
  # driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://www.lambdatest.com/selenium-playground/")
  print("Title: ", driver.title)

def test2_lambdatest_ecommerce(driver):
  # driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://ecommerce-playground.lambdatest.io/")
  print("Title: ", driver.title)

def testRexWebsite(driver):
  # driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://rexjones2.com")
  print("Title: ", driver.title)

# ignored by pytest
def google_test(driver):
  # driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://google.com")
  print("Title: ", driver.title)
