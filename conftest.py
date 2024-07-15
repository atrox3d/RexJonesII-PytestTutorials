import pytest
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection

from utilities.test_data import TestData

# params will pass each value as request.param to the fixture
# fixture reference: https://docs.pytest.org/en/7.1.x/reference/reference.html#pytest.fixture
# request object reference: https://docs.pytest.org/en/7.1.x/reference/reference.html#request
@pytest.fixture(params=[
                  "chrome", 
                  "firefox", 
                  # pytest.mark.xfail("edge", reason='edge web driver not working'),
                  "edge"
                ])
def initialize_driver(request):
  print("Browser: ", request.param)

  if request.param == "chrome":
    driver = webdriver.Chrome()
  elif request.param == "firefox":
    driver = webdriver.Firefox()
  elif request.param == "edge":
    pytest.skip(reason='microsoft edge webdriver not working under macos sonoma')
    driver = webdriver.Edge()
  #
  # add driver attribute to the calling class
  #
  request.cls.driver = driver
  #
  # get url from utility class
  #
  driver.get(TestData.url)
  driver.maximize_window()
  #
  # yields control
  #
  yield
  #
  # regain control and close driver
  #
  print("Close Driver")
  driver.close()

# 1st Step: Declare Variables For Setting Up LambdaTest
user_name = "Rex.Jones"
access_token = "YxU1eSK0Cx3WkN7d2FouJ4agNhPUiw8yOrXWAF8TN19LvOueVB"
remote_url = "https://" + user_name + ":" + access_token + "@hub.lambdatest.com/wd/hub"

# 2nd Step: Define The Desired Capabilities (3 Caps)
chrome_caps = {
  "build"       : "1.0",
  "name"        : "LambdaTest Grid On Chrome",
  "platform"    : "Windows 10",
  "browserName" : "Chrome",
  "version"     : "latest"
  }

firefox_caps = {
  "build"         : "2.0",
  "name"          : "LambdaTest Grid On Firefox",
  "platform"      : "Windows 10",
  "browserName"   : "Firefox",
  "version"       : "latest"
}

edge_caps = {
  "build"         : "3.0",
  "name"          : "LambdaTest Grid On Edge",
  "platform"      : "Windows 10",
  "browserName"   : "Edge",
  "version"       : "latest"
}

#3rd Step: Connect To LambdaTest Using A Fixture & RemoteConnection
@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver_initialization(request):
  """
  Initialize Driver For Selenium Grid On LambdaTest
  :param request:
  """
  desired_caps = {}

  if request.param == "chrome":
    desired_caps.update(chrome_caps)
    driver = webdriver.Remote(
      command_executor=RemoteConnection(remote_url),
      desired_capabilities={"LT:Options":desired_caps})
  elif request.param == "firefox":
    desired_caps.update(firefox_caps)
    driver = webdriver.Remote(
      command_executor=RemoteConnection(remote_url),
      desired_capabilities={"LT:Options": desired_caps})
  elif request.param == "edge":
    desired_caps.update(edge_caps)
    driver = webdriver.Remote(
      command_executor=RemoteConnection(remote_url),
      desired_capabilities={"LT:Options": desired_caps})
  request.cls.driver = driver
  yield
  driver.close()
