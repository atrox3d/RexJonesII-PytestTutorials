import pytest
import softest
from selenium import webdriver
from selenium.webdriver.common.by import By


class AssertionsTest(softest.TestCase):
  pass

  @pytest.mark.xfail(reason='testing failure')
  def test_lambdatest_radio_button_demo_value(self):
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
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
    print("Gender Object: \t", id(gender))
    print("Male Object: \t", id("Male"))
    self.soft_assert(self.assertIs,
    "Male", gender, "Gender Is Not Correct")
    self.soft_assert(self.assertTrue,
      driver.title.__contains__("Selenium Grid Online"))
    self.soft_assert(self.assertIn,
      "51", age_group, "Age Group Is Not Correct")
    self.assert_all("Verify Gender, Title, & Age Group")
