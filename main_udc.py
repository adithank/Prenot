import undetected_chromedriver as udc
import os 
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random

import telegram
import asyncio
import logging
from datetime import datetime

def startChrome():
    # Start the chrome instance 
    options = udc.ChromeOptions()
    options.headless = False
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = udc.Chrome(use_subprocess=True, options=options)
    driver.delete_all_cookies()

    return driver

def login(driver):
    email_box = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.ID, "login-email"))
    )
    password_box = driver.find_element(By.ID, "login-password")
    email_box.send_keys(email)

    password_box.send_keys(password)

    sleep(random.randint(1, 3))
    
    # Click login button
    button = driver.find_elements(
                By.XPATH, "//button[contains(@class,'button primary g-recaptcha')]"
            )
    button[0].click()

    sleep(random.randint(1, 3))

    # Go to booking tab 
    button =driver.find_element(By.XPATH, "//span[text()='Prenota']")    
    button.click()

    sleep(random.randint(1, 3))

    logging.info(
                    f"Timestamp: {str(datetime.now())} - Successfully logged in."
                )

def checkForAppt(driver):
        while True:
            # Click on Book 
            button = driver.find_elements(
                        By.CSS_SELECTOR, "[href='/Services/Booking/4996']"
                    )
            button[0].click()

            sleep(random.randint(1,5))

            # Wait for pop=up dialog 
            ok_dialog = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'jconfirm-buttons'))
            )

            # If successful, alter in telegram 
            if ok_dialog: 
                # print("Message page detected")
                ok_dialog.click()

                logging.info(
                    f"Timestamp: {str(datetime.now())} - Dialog box detected. Re-trying in 5-6 minutes."
                )

                sleep(random.randint(300,400))
                continue
            else:
                # Send a message
                # print("No message page")
                logging.info(
                    f"Timestamp: {str(datetime.now())} - Appt could be open."
                )
                send_telegram_msg("BOOK NOW!!")
                
                break
        
def send_telegram_msg(message):
    
    bot_token = "7171868311:AAFKK98ywDcc9miItSTGm99T7pweM6oP4ZY"
    chat_id = "7787352867"


    async def send_telegram_message(bot_token, chat_id, message):  # Define an async function
        try:
            bot = telegram.Bot(token=bot_token)
            await bot.send_message(chat_id=chat_id, text=message)  # Use await here!
            # print("Telegram message sent!")
            logging.info(
                    f"Timestamp: {str(datetime.now())} - Telegram message sent."
                )
        except Exception as e:
            # print(f"Error sending Telegram message: {type(e).__name__}: {e}")  # Print full error
            logging.info(
                    f"Timestamp: {str(datetime.now())} - Telegram message not sent."
                )
            logging.info(
                    f"Error sending Telegram message: {type(e).__name__}: {e}"
                )

    asyncio.run(send_telegram_message(bot_token, chat_id, message))

    
    

logging.basicConfig(
    format="%(levelname)s:%(message)s",
    level=logging.INFO,
    handlers=[logging.FileHandler(".\\out.log"), logging.StreamHandler(sys.stdout)],
)

email = "kmadith@gmail.com"
password = "1qSt6wroQA!2BG%V"

# Start and login using credentials
driver = startChrome()

# Go to the website 
driver.get("https://prenotami.esteri.it/")

# Enter password and click login
login(driver)

# Click on Schnegen visa booking every 5 minutes 
try:
    checkForAppt(driver)
except Exception as e:
    logging.info(f"Exception {e}")
    send_telegram_msg("Error in code. Check execution")
    

input("End of execution")




