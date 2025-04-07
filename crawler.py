from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 設定 Selenium 瀏覽器選項
options = Options()
options.add_argument('--headless')  # 無頭模式，避免打開瀏覽器界面

# 指定 WebDriver 路徑（根據實際情況調整）
driver_path = '/path/to/chromedriver'

# 開啟瀏覽器
driver = webdriver.Chrome(service=Service(driver_path), options=options)

# 這裡以開啟網站為範例
driver.get('https://www.example.com')

# 假設爬蟲是抓取頁面中的某個元素
element = driver.find_element(By.ID, 'some-id')
print(element.text)

# 等待一段時間，防止爬蟲過快結束
time.sleep(5)

# 關閉瀏覽器
driver.quit()
