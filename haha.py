from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your Chrome WebDriver
chrome_driver_path = "/usr/local/python/3.10.13/lib/python3.10/site-packages/chromedriver"

# URL of the Google Form
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdmg42A7EQmBUu_OSIMTmydixI6aBctiFntC96jWpzTRgHTbQ/viewform?usp=sf_link"

# Start Chrome WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open Google Form
driver.get(form_url)

# Wait for the form to load
time.sleep(5)

# Find and click on the "Preview" button to display all questions
preview_button = driver.find_element(By.XPATH, "//div[@aria-label='Preview']")
preview_button.click()

# Wait for the preview to load
time.sleep(5)

# Find all questions and store them
questions = driver.find_elements(By.CLASS_NAME, "freebirdFormviewerComponentsQuestionBaseRoot")

# Sort the questions
sorted_questions = sorted(questions, key=lambda x: x.location['y'])

# Print the sorted questions
for question in sorted_questions:
    print(question.text)

# Close the browser
driver.quit()
