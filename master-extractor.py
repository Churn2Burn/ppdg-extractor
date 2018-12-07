import os
import sys
import base64
import email
import email.utils
import re
import csv
import getpass
from PIL import Image
from datetime import datetime
from imaplib import IMAP4, IMAP4_SSL
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import config
import time

if os.name == 'nt':
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

# Connect to the server
if config.IMAP_SSL:
    mailbox = IMAP4_SSL(host=config.IMAP_HOST, port=config.IMAP_PORT)
else:
    mailbox = IMAP4(host=config.IMAP_HOST, port=config.IMAP_PORT)

# Log in and select the configured folder
mailbox.login(config.IMAP_USERNAME, config.IMAP_PASSWORD)
mailbox.select(config.FOLDER)

# Search for matching emails
status, messages = mailbox.search(None, '(FROM {})'.format(config.FROM_EMAIL))
if status == "OK":
    # Convert the result list to an array of message IDs
    messages = messages[0].split()

    if len(messages) < 1:
        # No matching messages, stop
        print("No matching messages found, nothing to do.")
        exit()

    # Open the CSV for writing
    with open('cards_' + datetime.now().strftime('%m-%d-%Y_%H%M%S') + '.csv', 'w', newline='') as csv_file:
        # Start the browser and the CSV writer
        browser = webdriver.Chrome(config.CHROMEDRIVER_PATH)
        csv_writer = csv.writer(csv_file)

        # Create a directory for screenshots if it doesn't already exist
        screenshots_dir = os.path.join(os.getcwd(), 'screenshots')
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        # For each matching email...
        for msg_id in messages:
            print("---> Processing message id {}...".format(msg_id.decode('UTF-8')))

            # Fetch it from the server
            status, data = mailbox.fetch(msg_id, '(RFC822)')

            if status == "OK":
                # Convert it to an Email object
                msg = email.message_from_bytes(data[0][1])

                # Get the HTML body payload
                config.FROM_EMAIL == "rewards@notifications.earnwithdrop.com"
                msg_html = msg.get_payload(1).get_payload(decode=True)

                # Save the email timestamp
                datetime_received = datetime.fromtimestamp(
                    email.utils.mktime_tz(email.utils.parsedate_tz(msg.get('date'))))

                # Parse the message
                msg_parsed = BeautifulSoup(msg_html, 'html.parser')

                # Find the "Claim Reward" link
                egc_link = msg_parsed.find("a", text="Claim Reward")
                if egc_link is not None:
                    # Open the link in the browser
                    browser.get(egc_link['href'])

                    # Get the type of card
                    card_type_exists = browser.find_elements_by_xpath('//*[@id="top-content2"]/h2[2]')

                    if card_type_exists:
                        card_type = browser.find_element_by_xpath('//*[@id="top-content2"]/h2[2]').text.strip()
                        card_type = re.compile(r'(.*) Terms and Conditions').match(card_type).group(1)

                    else:
                        input("Press Enter to continue...")
                        browser.find_element_by_css_selector('.roundbutton').click()
                        drop_string_1 = browser.find_element_by_xpath('//*[@id="top-content2"]/h2[2]').text.strip()
                        drop_string_2 = browser.find_element_by_xpath('//*[@id="top-content2"]/p').text.strip()

                        card_output = drop_string_1 + ',' + drop_string_2
                        card_output = re.search(r'\$(\d+(\.\d+)?).+For (.+),.+Code: (.+)', card_output).groups()

                        card_output[2] # brand
                        card_output[0] # denom
                        card_output[3] # code

                    # Save a screenshot
                    element = browser.find_element_by_xpath('//*[@id="top-content2"]')
                    location = element.location

                    size = element.size
                    screenshot_name = os.path.join(screenshots_dir, card_output[3] + '.png')
                    screenshot_name_new = os.path.join(screenshots_dir, card_output[3] + '.jpg')
                    browser.save_screenshot(screenshot_name)

                    im = Image.open(screenshot_name)
                    left = location ['x']
                    top = location['y']
                    right =  location['x'] + size['width']
                    bottom = location['y'] + size['height']

                    im = im.crop((left, top, right, bottom))
                    im.convert('RGB').save(screenshot_name_new)
                    sleep(0.1)
                    os.remove(screenshot_name)

                    # Write the details to the CSV
                    csv_writer.writerow([card_output[2],card_output[0],card_output[3]])

                    # Print out the details to the console
                    print("{}, {}, {}".format(card_output[2], card_output[0], card_output[3]))
                else:
                    print("ERROR: Unable to find eGC link in message {}, skipping.".format(msg_id.decode('UTF-8')))
            else:
                print("ERROR: Unable to fetch message {}, skipping.".format(msg_id.decode('UTF-8')))

            time.sleep(8)

        # Close the browser
        browser.close()
        print("")
        print("Thank you, come again!")
else:
    print("FATAL ERROR: Unable to fetch list of messages from server.")
    exit(1)