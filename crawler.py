from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # 在無頭模式下運行
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver_path = "/usr/bin/chromedriver"  # 更新為正確的路徑

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://example.com")
print(driver.title)
driver.quit()
