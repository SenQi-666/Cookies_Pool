from appium import webdriver
import time


class SMS:
    def __init__(self, phone_number, content):
        self.PhoneNumber = phone_number
        self.Content = content

    def send(self):
        try:
            print('正在向 %s 发送短信内容：%s，请稍后......' % (self.PhoneNumber, self.Content))
            desc = {
                'deviceName': 'fe46f757',
                'platformName': 'Android',
                'platformVersion': '9',
                'appPackage': 'com.android.mms',
                'appActivity': '.ui.NewMessageActivity'
            }
            driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desc)
            time.sleep(1)
            driver.find_element_by_accessibility_id("收信人: ").send_keys(self.PhoneNumber)
            driver.find_element_by_id("com.android.mms:id/embedded_text_editor").send_keys(self.Content)
            driver.find_element_by_accessibility_id("发送短信").click()
            time.sleep(2)
            print('短信发送完成！')
        except Exception:
            raise NotImplementedError('Please start the appium process first')
