from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
'''
STEP 1: instal selenium
pip install selenium
STEP 2: download chrome webdriver at https://chromedriver.chromium.org/downloads
STEP 3: add the chromedriver.exe in the same location as your script
STEP 4: run the script
python scraping.py
'''

chrome_options = Options()
chrome_options.add_argument("--headless") #for the chromedriver to run in background
driver = webdriver.Chrome(options=chrome_options)
url = 'https://sicurogroup.com'
driver.get(url)
time.sleep(5) #wait for 5 seconds - optional depends on site's loading speed
termsofbusiness = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div[1]/a[1]') #to get the xpath element - visit https://stackoverflow.com/questions/3030487/is-there-a-way-to-get-the-xpath-in-google-chrome
privacypolicy = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div[1]/a[2]')
print(termsofbusiness.text)
print(privacypolicy.text)
