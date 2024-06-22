# Text-based-CAPTCHA-Solver
A Simple Python-based Program which I have developed in Year 2022 to automate CAPTCHA solving process on my University Login Page Website.
The aim was to enhance my skills in web automation and image processing using Python.
> [!Important]
> <ins>**Disclaimer:**</ins>
> <br>
> This project/ program, including the text-based CAPTCHA solver, is developed strictly for educational and learning purposes. The aim is to explore and demonstrate techniques in web automation, image processing, and OCR using Python libraries such as Selenium, Pillow (Python Imaging Library), and Tesseract.
> 
> <ins>**Ethical Use:**</ins>
> <br>
> This project should only be used in accordance with ethical principles and for lawful purposes. It is not intended for any unethical or malicious activities, including but not limited to bypassing CAPTCHA protections without authorization, automated spamming, or any form of unauthorized access.
> 
> <ins>**Legal Compliance:**</ins>
> <br>
> Users are responsible for ensuring that their use of this project complies with all applicable laws and regulations. The project maintainers and contributors are not liable for any misuse or illegal activities conducted using this software.

## Key Features:
**Automation:**         Utilized <ins>**Selenium**</ins> for web interaction to navigate and interact with CAPTCHA-protected web pages.
<br>
**Image Processing:**   Utilized <ins>**Pillow (Python Imaging Library)**</ins> to preprocess CAPTCHA images for better OCR accuracy.
<br>
**OCR Integration:**    Utilized <ins>**Tesseract**</ins> for optical character recognition to decipher CAPTCHA images and automate form submissions.

## Flow of the program:
### Short Description:
- Define login credentials
- Navigate to the login page
- Enter a loop that does the following:
  - Wait for page elements to load
  - Enter Student ID and Password
  - Capture the CAPTCHA image
  - Use OCR to read the CAPTCHA text
  - Enter the CAPTCHA text
  - Submit the form
  - Check if login was successful
  - If not successful, refresh and try again
- After successful login, wait 10 seconds before closing
<br>

### Flowchart:
![CAPTCHA SOLVER drawio](https://github.com/Shen0003/Text-based-CAPTCHA-Solver/assets/173021017/d18d1f8f-3534-4833-81ce-713d84be4449)



