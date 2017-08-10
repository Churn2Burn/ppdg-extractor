import os
directory = os.path.dirname(os.path.abspath(__file__))
file = "chromedriver.exe"

CHROMEDRIVER_PATH = os.path.join(directory, file)

IMAP_HOST = "imap.gmail.com"
IMAP_PORT = 993
IMAP_SSL = True
IMAP_USERNAME = "GMAIL"
IMAP_PASSWORD = "PASSWORD"

FOLDER = "LABEL" 

FROM_EMAIL = "gifts@paypal.com"

card_amount = '//*[@id="main-content"]/div[3]/div/div[3]/section/div/div[1]/div/div/div/dl[1]/dd'
card_number = '//*[@id="main-content"]/div[3]/div/div[3]/section/div/div[1]/div/div/div/dl[2]/dd'
card_pin = '//*[@id="main-content"]/div[3]/div/div[3]/section/div/div[1]/div/div/div/dl[3]/dd'
