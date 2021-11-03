from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PROMISSED_SPEED = [YOUR_INTERNET_PROMISSED_SPEED]
USERNAME = [YOUR_USERNAME]
SENHA = [YOUR_PASSWORD]
CHROME_PATH = [PATH_TO_CHROMEDRIVER]

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path= CHROME_PATH)
        self.up = 0
        self.down = 0

    def getInternetSpeed(self):
        self.driver.get("https://www.speedtest.net/")
        self.start = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        self.start.click()
        time.sleep(60)
        div = self.driver.find_element(By.CSS_SELECTOR, "div.result-area")
        self.download = div.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.upload = div.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        return self.download

    def tweetAtProvider(self, download):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        self.driver.find_element(By.NAME, "username").send_keys(USERNAME)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span').click()
        time.sleep(3)
        self.driver.find_element(By.NAME, "password").send_keys(SENHA)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span').click()
        time.sleep(4)
        self.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Tweetar']").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "div[aria-label='Texto do Tweet']").send_keys(f"YOUR COMPLAINT WITH THE ACTUAL VELOCITY{download}.")
        self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='tweetButton']").click()

bot = InternetSpeedTwitterBot()

bot.getInternetSpeed()

if float(bot.getInternetSpeed()) < float(PROMISSED_SPEED):
    bot.tweetAtProvider(download=bot.download)
else:
    print("It's all good")


