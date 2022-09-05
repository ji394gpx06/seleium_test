
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def crowweb():
    from selenium import webdriver
ChromeDRVIER_PATH = 'chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument('blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(executable_path=ChromeDRVIER_PATH,
                          chrome_options=chrome_options
                         )
driver.get("https://www.google.com")
print(driver.title)
driver.close()
    #SP500=driver.find_elements(By.ID,("marketsummary-itm-0"))
    #for element in SP500:
     #   print(element.text)
    #Dow30=driver.find_elements(By.ID,("marketsummary-itm-1"))
    #for element in Dow30:
     #   print(element.text)
if __name__ == '__main__':
    crowweb()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
