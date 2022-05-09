import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import cv2
import base64



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Referer": "http://pic.netbian.com/4kmeinv/index.html"
}

# browser.get("https://www.gettyimages.com/")
# input = browser.find_element(By.XPATH,"/html/body/div[2]/section/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[1]/form/input")
# input.send_keys("kobe-bryant")
# input.send_keys(Keys.ENTER)
j = 122
for k in range(3, 101):
    browser = webdriver.Chrome()
    browser.get(
        'https://www.gettyimages.com/photos/kobe-bryant?family=editorial&assettype=image&phrase=kobe%20bryant&sort=mostpopular&page=' + str(k))
    imagesPart = browser.find_elements(By.TAG_NAME, "picture")
    for image in imagesPart:
        i = image.find_element(By.TAG_NAME, 'img')
        url = i.get_attribute('src')
        j += 1
        img_name = 'kd%d.png' % (j)
        with open('/Users/norahc/PycharmProjects/Computational_photography/Final_project/datasets_new/' + img_name,
                  'wb') as f:
            print(f"downloading：{img_name}")
            data = requests.get(url, headers)
            f.write(data.content)
        time.sleep(3)
    #     image.screenshot('/Users/norahc/PycharmProjects/Computational_photography/Final_project/datasets_new/kb%d.png' % (i))
    #     i += 1
    browser.close()

