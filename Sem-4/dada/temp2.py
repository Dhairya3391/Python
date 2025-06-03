from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

numbers_file = "numbers.txt"
image_path = "image.jpg"

with open(numbers_file) as f:
    numbers = [line.strip() for line in f if line.strip()]

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=./User_Data")  # reuse session to avoid QR scan every time
chrome_options.add_argument("--headless=new")  # Headless mode (for Chrome 109+)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://web.whatsapp.com/")
input("Scan QR in visible window (for first time), then press Enter here...")

for number in numbers:
    try:
        driver.get(f"https://web.whatsapp.com/send?phone={number}&text&app_absent=0")
        time.sleep(3)  # minimal wait for page load

        # Click attach button
        
        attach_btn = driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']")
        attach_btn.click()
        time.sleep(1)

        # Upload file
        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        file_input.send_keys(image_path)
        time.sleep(2)  # wait for upload preview

        # Send button
        send_btn = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_btn.click()

        print(f"Sent to {number}")
        time.sleep(1)  # minimal wait before next number

    except Exception as e:
        print(f"Failed to send to {number}: {e}")

driver.quit()
