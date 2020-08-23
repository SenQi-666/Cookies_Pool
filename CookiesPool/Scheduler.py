from multiprocessing import Process
from CookiesPool.Generator import *
from CookiesPool.Tester import *
from CookiesPool.API import app
from conf import Settings


class Dispatch:
    def __init__(self):
        self.GENERATOR_MAP = Settings.GENERATOR_MAP
        self.TESTER_MAP = Settings.TESTER_MAP
        self.HOST = Settings.API_HOST
        self.PORT = Settings.API_PORT
        self.GENERATOR_ENABLED = Settings.GENERATOR_ENABLED
        self.TESTER_ENABLED = Settings.TESTER_ENABLED
        self.API_ENABLED = Settings.API_ENABLED
        self.PHONE_NUMBER = str(Settings.PHONE_NUMBER)

    def cookies_generate(self):
        print('开始生成Cookies......')
        try:
            if self.PHONE_NUMBER is None:
                raise ValueError('Please enter your PhoneNumber in conf/Settings.py')
            for website, cls in self.GENERATOR_MAP.items():
                print('%s 站点的Cookies正在生成中，请稍后......' % website)
                getattr(eval(cls + '("'+website+'", "'+self.PHONE_NUMBER+'"'+')'), 'run')()
                print('%s 站点的Cookies全部生成并保存完成' % website)
        except Exception as e:
            print(e.args[0])

    def cookies_tester(self):
        print('开始检测Cookies......')
        try:
            for website, cls in self.TESTER_MAP.items():
                print('正在检测 %s 站点的Cookies，请稍后......' % website)
                getattr(eval(cls + '("'+website+'"'+')'), 'run')()
                print('%s 站点的Cookies全部检测完成' % website)
        except Exception as e:
            print(e.args)

    def api(self):
        print('API接口开始运行......')
        app.run(host=self.HOST, port=self.PORT)

    def run(self):
        if self.GENERATOR_ENABLED:
            generator_process = Process(target=self.cookies_generate)
            generator_process.start()

        if self.TESTER_ENABLED:
            tester_process = Process(target=self.cookies_tester)
            tester_process.start()

        if self.API_ENABLED:
            api_process = Process(target=self.api)
            api_process.start()
