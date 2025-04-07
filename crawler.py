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

print("爬蟲開始運行...")  # 這裡加入日誌輸出

# 這裡以開啟網站為範例
driver.get('https://www.example.com')

# 假設爬蟲是抓取頁面中的某個元素
try:
    element = driver.find_element(By.ID, 'some-id')
    print("抓取到的元素文本:", element.text)
except Exception as e:
    print(f"抓取元素時出錯: {e}")

# 等待一段時間，防止爬蟲過快結束
time.sleep(5)

print("爬蟲運行結束。")  # 這裡加入日誌輸出

# 關閉瀏覽器
driver.quit()
