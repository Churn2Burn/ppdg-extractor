# ppdg-extractor
Extract (CSV) codes from and screenshot (JPG) PayPal Digital Gifts gift cards. Adapted from https://github.com/stevenmirabito/ code in order to clean up screenshots, save screenshots as .JPG, and to process PIN and non-PIN cards using the same program.

Program specifically configured on Windows - includes ChromeDriver.exe - for gmail.

1) Install Python 3.6.1

2) Open command prompt (cmd) and run the following commands:
	a) pip3 install requests
	
	b) pip3 install bs4
	
	c) pip3 install selenium
	
	d) pip3 install image

3) Edit config.py file:
	a) Change CHROMEDRIVER_PATH to location of this folder
	
	b) Change IMAP_USERNAME to your gmail account
	
	c) Change IMAP_PASSWORD to your gmail password
	
	d) Note: When logging in for the first time, gmail may block access. You will need to follow the steps in the email to follow to enable less secure applications.
	
	e) Create a gmail label for the cards you would like to extract and change FOLDER to this label.
	
4) Double click on MasterExtractor.bat to run the program. You will get .jpg screenshots in the "screenshots" folder and will have a .csv file with near GCW (GiftCardWiki) submission standards.

5) Enjoy!
