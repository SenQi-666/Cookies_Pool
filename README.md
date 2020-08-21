## Cookies Pool

------

可扩展的Cookies池，提供接口，目前针对新浪微博对接 [m.weibo.cn](m.weibo.cn)，如扩展其他站点可自行修改

### 目录

### 使用前请安装依赖

------

```shell
pip3 install -r requirements.txt
```

#### 由于新浪微博小号需要发送短信验证即可登陆，所以用到 Appium 控制手机发送短信，一定程度上也增大了运行速度（资源有限，搞不了手机集群），而 Appium 使用之前也依赖一些环境： Java JDK、Android ADB。自行Google





