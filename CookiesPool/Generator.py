from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from CookiesPool.RedisControl import RedisClient
from CookiesPool.weibo.PhoneSMS import SMS
from selenium import webdriver
from conf import Settings
import time
import json


class BasicGenerator:
    def __init__(self, website):
        self.DB_ACCOUNT = RedisClient(website, 'Account')
        self.DB_COOKIES = RedisClient(website, 'Cookies')
        self.GENERATOR_DELAY = Settings.GENERATOR_DELAY

    def get_account(self):
        users = self.DB_ACCOUNT.all_usr()
        for user in users:
            yield user

    def save_cookie(self, usr, cookies):
        self.DB_COOKIES.set(usr, cookies)

    def generate(self, *args):
        raise SyntaxError('Please overwrite the <Function generate>')

    def run(self, *args):
        raise SyntaxError('Please overwrite the <Function run>')


class WeiBoCookiesGenerator(BasicGenerator):

    def __init__(self, website, phone_umber):
        super(WeiBoCookiesGenerator, self).__init__(website)
        self.website = website
        self.phone_number = phone_umber
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-automation'])
            self.driver = webdriver.Chrome(options=options)
        except Exception:
            raise Exception('Please configure the Chrome first')

    def generate(self, account, phone_number):
        usr, pwd = account, self.DB_ACCOUNT.get(account)
        self.driver.delete_all_cookies()
        self.driver.get(Settings.GENERATOR_LOGIN_URL[self.website])
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'loginName'))).send_keys(usr)
        self.driver.find_element_by_id('loginPassword').send_keys(pwd)
        self.driver.find_element_by_id('loginAction').click()
        time.sleep(3)
        if self.driver.find_elements_by_class_name('geetest_radar_tip'):
            print('请人工点击认证或滑动滑块')
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'nav_item')))
        else:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vdVerify"]/div[1]/div/div/div[4]/span/a'))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vdVerify"]/div[3]/div[2]/div[1]/div/div[1]/div/a')))\
                .click()
            wait.until(EC.presence_of_element_located((
                By.XPATH,
                '//*[@id="others"]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/span/input'
            ))).send_keys(phone_number)
            self.driver.find_element_by_class_name('m-btn').click()
            SMS('1069009010021', 'DLYZ').send()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="msgVerify"]/div[1]/div/div/div[2]/a[2]').click()
        cookies = self.driver.get_cookies()
        cookies = json.dumps(cookies[0])
        print(cookies)
        self.save_cookie(usr, cookies)

    def run(self):
        accounts = self.get_account()
        for account in accounts:
            if account not in self.DB_COOKIES.all_usr():
                print('正在为账号：%s 生成Cookie......请稍后...' % account)
                self.generate(account, self.phone_number)
                print('账号：%s 生成Cookie成功！已保存！' % account)
                time.sleep(self.GENERATOR_DELAY)
        self.driver.close()
