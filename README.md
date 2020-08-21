## Cookies Pool

------

可扩展的Cookies池，提供接口，目前针对新浪微博对接 [m.weibo.cn](m.weibo.cn)，如扩展其他站点可自行修改

### 目录

------

```
├── CookiesPool

│  ├── API.py

│  ├── Generator.py

│  ├── RedisControl.py

│  ├── SaveAccount.py

│  ├── Scheduler.py

│  ├── Tester.py

│  ├── __init__.py

│  ├── __pycache__

│  │  ├── RedisControl.cpython-36.pyc

│  │  ├── Scheduler.cpython-36.pyc

│  │  └── __init__.cpython-36.pyc

│  └── weibo

│    ├── PhoneSMS.py

│    ├── __init__.py

│    └── __pycache__

│      ├── PhoneSMS.cpython-36.pyc

│      └── __init__.cpython-36.pyc

├── README.md

├── __pycache__

├── bin

│  ├── Generate_Account_File.py

│  ├── __init__.py

│  └── run_project.py

├── conf

│  ├── Settings.py

│  └── __init__.py

├── libs

│  └── weibo_account.txt

└── requirements.txt
```



### 使用前请安装依赖

------

```shell
$ pip3 install -r requirements.txt
```

由于新浪微博小号现如今需要发送短信验证才可登陆，所以之前的Cookies池现已删除。池中用到 Appium 控制手机发送短信，一定程度上也增大了运行速度（资源有限，搞不了手机集群）。而 Appium 使用之前也依赖一些环境： Java JDK、Android ADB，安装过程自行Google。



### 基础配置

------

#### 程序基本配置

在 conf/Settings.py 修改

```python
# 生成器类，如扩展其他站点可在此配置
GENERATOR_MAP = {
    'weibo': 'WeiBoCookiesGenerator',
    # 'taobao': 'TaoBaoCookiesGenerator',
}

# 检测器类，如扩展其他站点可在此配置
TESTER_MAP = {
    'weibo': 'WeiBoCookiesTester',
    # 'TaoBao': 'TaoBaoCookiesTester',
}

# 生成器站点登陆网址，如扩展其他站点可在此配置
GENERATOR_LOGIN_URL = {
    'weibo': 'https://passport.weibo.cn/signin/login',
    # 'TaoBao': 'https://login.taobao.com/',
}

# 测试器测试网址，如扩展其他站点可在此配置
TESTER_URL = {
    'weibo': 'https://m.weibo.cn/profile/5014846080',
    # 'TaoBao': '',
}

# 生成器延迟，数字越大速度越慢
GENERATOR_DELAY = 2

# 检测器延迟，数字越大速度越慢
TESTER_DELAY = 2

# Redis数据库地址
REDIS_HOST = 'localhost'

# Redis数据库端口
REDIS_PORT = 6379

# Redis数据库密码，如无填None
REDIS_PASSWORD = None

# API接口地址
API_HOST = '0.0.0.0'

# API接口端口
API_PORT = 5000

# 生成器开关，生成Cookies
GENERATOR_PROCESS = True

# 检测器开关，检测Cookies是否可用
TESTER_PROCESS = True

# API接口服务
API_PROCESS = True

# 您的手机号，用于控制手机发送短信登陆账号，如不需要填None（目前微博需要，其他站点自行斟酌）
PHONE_NUMBER = None
```



### 微博小号

------

一些平台以及某宝有售



### 运行

------

#### 运行之前首先创建账号存储文件

```shell
$ cd bin
$ python3 Generate_Account_File.py website
```

website 为站点参数



#### 创建好的txt文件

------

位于 libs 文件夹内，数据格式为：

```
账号----密码
账号----密码
账号----密码
```



#### 运行Cookie池

------

```shell
$ python3 run_project.py
```

