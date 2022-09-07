
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
def crowweb():
    from selenium import webdriver
    ChromeDRVIER_PATH = 'chromedriver'
    Service = ChromeService(executable_path=ChromeDRVIER_PATH,)
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(service=Service,
                          options=chrome_options
                         )
    driver.get("https://www.google.com")
    print(driver.title)
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
