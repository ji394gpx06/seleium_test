# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ChromeDRVIER_PATH = '/Users/ruijun/PycharmProjects/pythonProject/chromedriver'

def crowweb():
    chrome_options = Options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 啟動Headless 無頭
    chrome_options.add_argument('--disable-gpu') #關閉GPU 避免某些系統或是網頁出錯
    driver = webdriver.Chrome(executable_path=ChromeDRVIER_PATH,chrome_options=chrome_options)

    driver.get("https://finance.yahoo.com/watchlists/")
    SP500=driver.find_elements_by_id("marketsummary-itm-0")
    for element in SP500:
        print(element.text)
    Dow30=driver.find_elements_by_id("marketsummary-itm-1")
    for element in Dow30:
        print(element.text)
    driver.close()
if __name__ == '__main__':
    crowweb()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
