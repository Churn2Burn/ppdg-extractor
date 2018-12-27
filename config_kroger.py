import os
directory = os.path.dirname(os.path.abspath(__file__))

#file = 'chromedriver.exe' #Windows
file = 'chromedriver.dmg' #Mac

CHROMEDRIVER_PATH = os.path.join(directory, file)

IMAP_HOST = 'imap.gmail.com'
IMAP_PORT = 993
IMAP_SSL = True
IMAP_USERNAME = 'USERNAME'
IMAP_PASSWORD = 'PASSWORD'

FOLDER = 'Kroger'


# subject 'You have received a gift card from [Name]'
#FROM_EMAIL = 'gcm-cust-serv@giftcardmall.com'

#subject 'Your Order is Complete'
FROM_EMAIL = 'customerservice@giftcardmall.com'
#Bookstore@giftcardmall.com

card_amount = [('//*[@id="amount"]', '$'), ('//*[@id="value"]', 'eCard Amount: $')]
card_number = '//*[@id="cardNumber2"]'
card_pin = [('//*[@class="cardNum"]/p[2]/span',''), ('//*[@id="securitycode"]', 'Pin #: '), ('//*[@text() = "Pin:"]/span', '')]
