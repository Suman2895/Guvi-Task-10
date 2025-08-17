from selenium import webdriver                  # imports the selenium webdriver module to the current project
from selenium.webdriver.common.by import By     # imports the By class to locate the web element
import time
import pytest

driver= webdriver.Chrome()                  # Launch a new Chrome browser window using selenium
driver.maximize_window()

driver.get("https://www.saucedemo.com/")       # Opens a URL in the browser of selected webpage

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.NAME,"login-button").click()

time.sleep(3)

driver.quit()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()       # closes the browser and ends the session

def test_homepage_title(driver):
    driver.get("https://www.saucedemo.com/")
    assert driver.title == "Swag Labs"

def test_homepage_url(driver):
    driver.get("https://www.saucedemo.com/")
    assert driver.current_url == "https://www.saucedemo.com/"

def test_dashboard_url_after_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    time.sleep(3)

    title = driver.title  # Title of the webpage
    print("\n Title of the page:", title)
    currentUrl = driver.current_url  # Current URL of the webpage
    print("Current URL:", currentUrl)
    PageSource = driver.page_source  # To Extract entire HTML content
    with open("Task_10.txt", "w", encoding="utf-8") as file:
        file.write(PageSource)

