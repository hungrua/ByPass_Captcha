from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from selenium.webdriver.common.by import By
from onest_captcha import OneStCaptchaClient

APIKEY = "cfa9d2330606422fa5b2616282ee0ce0"
client = OneStCaptchaClient(apikey=APIKEY)


if __name__ == "__main__":
    chrome_service = ChromeService(executable_path="C:/Users/Hung Nguyen/Desktop/Học Tập/ByPassCaptcha/Text-based Captcha/chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service)
    driver.get("https://www.google.com/recaptcha/api2/demo")
    sleep(3)
    url = "https://www.google.com/recaptcha/api2/demo"
    result = client.recaptcha_v2_enterprise_task_proxyless(site_url=url, site_key="6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-")
    if result["code"] == 0:  # success:
        print(result["token"])
        key = result["token"]
        textArea = driver.find_element(By.CLASS_NAME,"g-recaptcha-response")
        block = 'block'
        driver.execute_script("arguments[0].style.display = 'block';", textArea)
        sleep(3)
        textArea.clear()
        textArea.send_keys(key)
        sleep(3)
        driver.find_element(By.ID,"recaptcha-demo-submit").click()
    else:  # wrong
        print(result["messeage"])
    input("DONE")