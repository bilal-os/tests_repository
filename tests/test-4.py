import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

executor_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8888/"
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Remote(command_executor=executor_url, options=chrome_options)

try:
    driver.get("https://www.w3schools.com/html/html_buttons.asp")
    button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Click Me!']"))
    )
    assert button.text == "Click Me!", "Button text does not match expected value."
    print("Test passed: W3Schools button text verified successfully.")
except Exception as e:
    print("Test failed:", e)
finally:
    driver.quit()
