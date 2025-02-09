import configparser
import time
import os
import sys
import random

import telegram
import asyncio

from datetime import datetime
from modules import Browser
from modules import PrenotPage

from selenium.common.exceptions import TimeoutException

def send_telegram_msg(message):
    
    bot_token = "7171868311:AAFKK98ywDcc9miItSTGm99T7pweM6oP4ZY"
    chat_id = "7787352867"


    async def send_telegram_message(bot_token, chat_id, message):  # Define an async function
        try:
            bot = telegram.Bot(token=bot_token)
            await bot.send_message(chat_id=chat_id, text=message)  # Use await here!
            print("Telegram message sent!")
        except Exception as e:
            print(f"Error sending Telegram message: {type(e).__name__}: {e}")  # Print full error

    asyncio.run(send_telegram_message(bot_token, chat_id, message))


def gotoLinkAndLogIn():

        
   # Locate login form
    loc = prenot.get_locator('login')

    if loc:
        EMAIL = "kmadith@gmail.com"
        PASSWORD = "1qSt6wroQA!2BG%V"

        # Search for the e-mail field and fill it
        browser.find_fill_submit(by=loc['BY'], 
                                    value=loc['LOGIN_EMAIL'], 
                                    keys=EMAIL)

        # Search for the pass field, fill it and submit the form
        browser.find_fill_submit(by=loc['BY'], 
                                    value=loc['LOGIN_PASSWORD'], 
                                    keys=[PASSWORD, 'RETURN'])

        # Delete the variable
        del(loc)

    ok_dialog=browser.find_elements(by='class_name',value = 'jconfirm-buttons')
    
    return ok_dialog 


sleeptime = 30

while True:

    # Create the instance of the browser
    browser = Browser.Browser(True)

    prenot = PrenotPage.PrenotPage()


    browser.go_to(url=prenot.get_url())

    try:
        ok_dialog = gotoLinkAndLogIn()

        if ok_dialog: 
            print("Message page detected")
            ok_dialog[0].click()
            time.sleep(sleeptime)
            browser.close_browser()
            continue
        else:
            # Send a message
            print("Error in clicking OK")
            send_telegram_msg("BOOK NOW!!")
            time.sleep(sleeptime)
            browser.close_browser()
            continue

    except:
        print("Error. ")
        # send_telegram_msg("!!")
        time.sleep(sleeptime)
        browser.close_browser()
        continue


