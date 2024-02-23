import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class alerte(unittest.TestCase):
    JS_ALERT_LOCK=(By.CSS_SELECTOR,'[onclick=\'jsAlert()\']')
    RESULT_LOC = (By.CSS_SELECTOR,'')
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.URl = 'https://the-internet.herokuapp.com/javascript_alerts'
        self.chrome.get(self.URL)
        self.chrome.implicitly_wait(5)
    def tearDown(self) -> None:
        print('Eliberam drive-ul')
        self.chrome.quit()
    def testJSAlert(self):
        self.chrome.find_element(*self.JS_ALERT_LOCK).click()
        self.chrome.switch_to.alert.accept()
        time.sleep(1)

