import os
directory = os.path.dirname(os.path.abspath(__file__))

file = 'chromedriver.exe' #Windows
#file = 'chromedriver.dmg' #Mac

CHROMEDRIVER_PATH = os.path.join(directory, file)

# Email Settings
IMAP_HOST = 'imap.gmail.com'
IMAP_PORT = 993
IMAP_SSL = True
IMAP_USERNAME = 'XXXXXXXXXX'
IMAP_PASSWORD = 'XXXXXXXXXX'

FOLDER = 'XXXXXXXXXX'

FROM_EMAILS = ['gifts@paypal.com', 'no-reply@samsungpay.com']

# Gift Card Settings
card_amount = '//*[@id="app"]/div/div/div/div/section/div/div[1]/div[2]/div/dl[1]/dd'
card_number = '//*[@id="app"]/div/div/div/div/section/div/div[1]/div[2]/div/dl[2]/dd'
card_pin = '//*[@id="app"]/div/div/div/div/section/div/div[1]/div[2]/div[2]/dl[3]/dd'

SAVE_SCREENSHOTS = True

# CSV Output Formats:
# TCB: card_number, card_pin, card_amount
# GCW: card_amount, card_number, card_pin
CSV_OUTPUT_FORMAT = "TCB"

