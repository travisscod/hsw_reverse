from undetected_chromedriver import Chrome, ChromeOptions
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

c = ChromeOptions()
#c.add_argument("--headless")

req = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmIjowLCJzIjoyLCJ0IjoidyIsImQiOiJwS3ptZzRXR3pHc0dMTmJJaE1YWENQckdmSUNvbSt5SGNraVNzektKV1ZpREhvdHgzWHRDZk1pVnNFTUZKQ2YzNTRTazBPNzlwVVVMSDNQQ2tPZllLbEc3em42OW9udGhOVCtXWm5kM3JKYmExdTcycXpUMnIyTGZLcHNVVnVqaFpmOFhsVE9yWHBmY0YxU09HOHd6OW5iWWFLaWM2UmFPVVJQOXJja3VpaHBPWUhYNmJ2MlVDdEkzamxzc3QzbFlZU25YUUF3eXROWHVJSEV4NEM0S3ZHZlpNSEJHV09zYXpybzE1cHZFcFFGZ01TTjJwQmFMMUYwY0lWUnF2VmZIIiwibCI6Imh0dHBzOi8vbmV3YXNzZXRzLmhjYXB0Y2hhLmNvbS9jL2Y5MjJhNDEiLCJpIjoic2hhMjU2LVF0bWtBUnJEYXVTRDZPUExTN0t6Z3B1V3Z6WnJ2QndPS3JRTlRYM3Jra0E9IiwiZSI6MTcxNDk4MzE1MSwibiI6ImhzdyIsImMiOjEwMDB9.NOkj_70hpXIPqKrM223XDAFYHfSTYcrghKIFdbtQFYs"
    

c.add_argument("--disable-gpu")
c.add_argument("--disable-extensions")
c.add_argument("--no-sandbox")
driver = Chrome(service=Service(), options=c)

driver.get("http://127.0.0.1:5000")  



time.sleep(999999)