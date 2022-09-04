# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

ChromeDRVIER_PATH = '/usr/local/bin/chromedriver'

def crowweb():
    chrome_options = Options()
    WINDOW_SIZE = "1920,1080"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=ChromeDRVIER_PATH,chrome_options=chrome_options)

    driver.get("https://finance.yahoo.com/watchlists/")
    SP500=driver.find_elements(By.ID,("marketsummary-itm-0"))
    for element in SP500:
        print(element.text)
    Dow30=driver.find_elements(By.ID,("marketsummary-itm-1"))
    for element in Dow30:
        print(element.text)
    driver.close()
if __name__ == '__main__':
    crowweb()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
