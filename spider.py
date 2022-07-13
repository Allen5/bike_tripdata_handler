## get bike data links
from asyncore import write
import csv
from lib2to3.pgen2 import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开页面
driver = webdriver.Chrome()
driver.get("https://s3.amazonaws.com/tripdata/index.html")

# 获取链接
WebDriverWait(driver, 20).until(EC.presence_of_element_located( (By.TAG_NAME, "a") ))
elements = driver.find_elements(by=By.TAG_NAME, value="a")
with open("./datas/files.csv", 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['name', 'link'])
    for el in elements:
        if ".zip" in el.text:
            writer.writerow([el.text, "https://s3.amazonaws.com/tripdata/" + el.text])