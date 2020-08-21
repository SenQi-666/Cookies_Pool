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
PHONE_NUMBER = '18132386942'
