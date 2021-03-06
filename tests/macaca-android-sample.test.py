#coding:utf-8

import unittest
import os
import time
from macaca import WebDriver

desired_caps = {
    'platformName': 'android',
    'app': 'https://npmcdn.com/android-app-bootstrap@latest/android_app_bootstrap/build/outputs/apk/android_app_bootstrap-debug.apk',
    'reuse': 3
}

server_url = {
    'hostname': 'localhost',
    'port': 3456
}

def switch_to_webview(driver):
    contexts = driver.contexts
    driver.context = contexts[-1]
    return driver

def switch_to_native(driver):
    contexts = driver.contexts
    driver.context = contexts[0]
    return driver

class MacacaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.driver.init()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_login(self):
        self.driver \
            .element_by_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.EditText[1]') \
            .send_keys('中文+Test+12345678')   \

        els = self.driver \
            .elements_by_class_name('android.widget.EditText')

        els[1].send_keys('111111')

        self.driver \
            .element_by_name('Login') \
            .click()

    def test_02_scroll_tableview(self):
        self.driver              \
            .element_by_name('HOME') \
            .click()

        self.driver             \
            .element_by_name('list') \
            .click()

    def test_03_gesture(self):
        self.driver \
            .touch('drag', {
              'fromX': 200,
              'fromY': 400,
              'toX': 200,
              'toY': 100,
              'steps': 50
            })

        time.sleep(1)

        self.driver \
            .touch('drag', {
              'fromX': 100,
              'fromY': 100,
              'toX': 100,
              'toY': 400,
              'steps': 50
            })

        self.driver \
            .element_by_name('Alert') \
            .click()

        time.sleep(1)

        self.driver \
            .accept_alert() \
            .back()

        time.sleep(1)

        self.driver \
            .element_by_name('Gesture') \
            .click()

        self.driver \
            .touch('tap', {
              'x': 100,
              'y': 100
            })

        time.sleep(1)

        self.driver \
            .touch('doubleTap', {
              'x': 100,
              'y': 100
            })

        time.sleep(1)

        self.driver \
            .touch('press', {
              'x': 100,
              'y': 100,
              'steps': 100
            })

        time.sleep(1)

        self.driver \
            .element_by_id('com.github.android_app_bootstrap:id/info') \
            .touch('pinch', {
              'percent': 200,
              'steps': 200
            })

        time.sleep(1)

        self.driver \
            .touch('drag', {
              'fromX': 100,
              'fromY': 100,
              'toX': 100,
              'toY': 600,
              'steps': 100
            })

        time.sleep(1)

        self.driver.back()

        time.sleep(1)

        self.driver.back()

    def test_04_webview(self):
        self.driver \
            .wait_for_element_by_name('Webview') \
            .click()

        time.sleep(3)
        self.driver.save_screenshot('./webView.png') # save screen shot

        switch_to_webview(self.driver) \
            .element_by_id('pushView') \
            .touch('tap')

        switch_to_webview(self.driver) \
            .element_by_id('popView') \
            .touch('tap')

    def test_05_web(self):
        switch_to_native(self.driver) \
            .element_by_name('Baidu') \
            .touch('tap')

        time.sleep(3)
        self.driver.save_screenshot("./baidu.png")

        switch_to_webview(self.driver) \
            .element_by_id('index-kw') \
            .send_keys('macaca')

        self.driver \
            .element_by_id('index-bn') \
            .touch('tap')

    def test_06_logout(self):
        switch_to_native(self.driver) \
            .element_by_name('PERSONAL') \
            .click()

        self.driver.element_by_name('Logout') \
            .click()

if __name__ == '__main__':
    unittest.main()
