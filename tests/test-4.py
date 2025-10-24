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
    driver.get("https://www.python.org")
    WebDriverWait(driver, 10).until(EC.title_contains("Python"))
    assert "Python" in driver.title, "Title verification failed for Python.org."

    print("Test passed: Python.org title verified successfully.")
except Exception as e:
    print("Test failed:", e)
finally:
    driver.quit()
