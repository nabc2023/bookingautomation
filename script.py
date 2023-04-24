import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# set up the Chrome driver
driver = webdriver.Chrome()

# navigate to the website
driver.get("https://www.example.com")

# set up email parameters
sender_email = "sender@example.com"
recipient_email = "recipient@example.com"
email_subject = "Interview slot available!"
email_body = "A slot is available for your interview. Book it now!"

# set up the email message
email_message = MIMEText(email_body)
email_message['Subject'] = email_subject
email_message['From'] = sender_email
email_message['To'] = recipient_email

# set up the email server
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_username = "your_username"
smtp_password = "your_password"

# wait for the slot to become available
while True:
    try:
        book_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Book interview')]"))
        )
        break
    except:
        driver.refresh()

# send email notification
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, recipient_email, email_message.as_string())

# click the book button
book_button.click()

# close the browser
driver.quit()
