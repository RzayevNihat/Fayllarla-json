from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_options = Options()
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get("https://userinyerface.com/game.html")

element1 = driver.find_element(By.CLASS_NAME, 'login-form__field-row')
print(element1.value_of_css_property("width") == "372px")

element2 = driver.find_element(By.CLASS_NAME, 'login-form__field-row')
print(element2.value_of_css_property("height") == "40px")

element2 = driver.find_element(By.CLASS_NAME, 'align__cell')
print(element2.value_of_css_property("width") == "133.688px")

element2 = driver.find_element(By.CLASS_NAME, 'login-form__container')
print(element2.value_of_css_property("font-family") == "sans-serif")

element2 = driver.find_element(By.CLASS_NAME, 'login-form__container')
print(element2.value_of_css_property("background") == "#fff")
# driver.get("https://www.youtube.com/")
# search=driver.find_element()
time.sleep(10)