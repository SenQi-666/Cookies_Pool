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
│  └── weibo
│    ├── PhoneSMS.py
│    ├── __init__.py
├── README.md
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

>>>>>>> 57555cb0149e095f0cd742213250b61943f9f48d
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


#### 运行效果

------

三个进程全部开启

```
开始生成Cookies......
weibo 站点的Cookies正在生成中，请稍后......
开始检测Cookies......
正在检测 weibo 站点的Cookies，请稍后......
API接口开始运行......
 * Serving Flask app "CookiesPool.API" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
weibo 站点的Cookies全部检测完成
正在为账号：16521576842 生成Cookie......请稍后...
正在向 1069009010021 发送短信内容：DLYZ，请稍后......
短信发送完成！
{"domain": "passport.weibo.cn", "expiry": 1598083611, "httpOnly": true, "name": "FID", "path": "/", "secure": true, "value": "2OWRfQM6TAAPfyvIq8VxlThHveg7KrpQCBWxvZ2lu"}
账号：16521576842 生成Cookie成功！已保存！
正在为账号：17087169435 生成Cookie......请稍后...
请人工点击认证或滑动滑块
{"domain": ".weibo.cn", "expiry": 1598086341, "httpOnly": false, "name": "MLOGIN", "path": "/", "secure": false, "value": "1"}
账号：17087169435 生成Cookie成功！已保存！
weibo 站点的Cookies全部生成并保存完成
```
