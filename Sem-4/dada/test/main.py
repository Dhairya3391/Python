from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Navigate to a test website
    driver.get("https://www.example.com")
    
    # Print page title to verify
    print("Page title:", driver.title)
    
    # Wait for 3 seconds to see the browser
    time.sleep(3)
    
    # Close the browser
    driver.quit()
    
    print("Selenium is working correctly!")
    
except Exception as e:
    print("Error: Selenium is not working. Details:", str(e))