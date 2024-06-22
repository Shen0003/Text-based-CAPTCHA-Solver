from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
import time

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize Chrome WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Credentials
Student_ID: str = "ENTER YOUR Student_ID HERE" # CHANGE HERE
Password: str = "ENTER YOUR PASSWORD HERE"     # CHANGE HERE
Check: bool = True

# Load login page
driver.get("https://unitreg.utar.edu.my/portal/courseRegStu/login.jsp")

try:
    while Check:
        # Wait for elements to load
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "reqFregkey")))
        
        # Input Student_ID by program
        input_element_id = driver.find_element(By.NAME, "reqFregkey")
        input_element_id.clear()
        input_element_id.send_keys(Student_ID)

        # Input Password by program
        input_element_passw = driver.find_element(By.NAME, "reqPassword")
        input_element_passw.clear()
        input_element_passw.send_keys(Password)

        # Locate and capture CAPTCHA image
        captcha_image = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//img[contains(@src, "Kaptcha.jpg")]'))
        )
        captcha_image.screenshot('captcha.png')

        # Process CAPTCHA image (by Tesseract OCR)
        image = Image.open('captcha.png')
        captcha_text = pytesseract.image_to_string(image).strip()
        print(f"Captcha text: {captcha_text}")

        # Input CAPTCHA text by program
        input_element_kaptcha = driver.find_element(By.NAME, "kaptchafield")
        input_element_kaptcha.clear()
        input_element_kaptcha.send_keys(captcha_text)

        # Click Submit by program
        input_element_kaptcha.submit()

        # Check if login is successful by examining the URL
        if "dashboard" in driver.current_url:
            print("Successfully logged in!")
            Check = False  # Exit the loop if login is successful
        else:
            print("Retrying...")
            driver.refresh() # Refresh the webpage and loop again

    # Pauses the program for 10 second after login sucessfully
    print("Successfully completed process, waiting for 10 seconds before closing...")
    time.sleep(10)

finally:
    # Close the WebDriver and quit the browser
    driver.quit()
