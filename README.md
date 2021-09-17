# Godscan
# 项目简介

​		通过学习 python 编程语言， 进而对常见 web 漏洞 poc 进行收集编写，使得能进行一键化检测及利用。于是通过pyqt5 开发加载 poc 脚本框架以便更好利用漏洞，简单功能实现如下：



**获取扫描地址 ---> 加载漏洞检测脚本 ---> 输出检测结果 ---> 一键利用命令执行和反弹**     



* poc 涉及漏洞基本信息和参考地址   

  主要参看 https://vulhub.org/ 及各安全论坛及博客

* poc 会做好分类自动化获取分类

吾将 poc 脚本框架命名为 **GodScan**



# 显示模块

​		分为三个模块，漏洞检测、漏洞利用、编码解码等



## 漏洞检测

显示设置 --> 可以设置显示全部、存在、不存在三种情况显示，并且增加颜色显示效果，漏洞存在显示红色，漏洞等级显示，高危 -->红色、 中危 -->黄色、底危 -->绿色。

界面 -- 增加主题效果 

设置 --> 自动获取 ua 等请求头，也可自定义。

具体效果如下：

线程暂无法使用， 等以后进行优化

![image-20210917165656350](C:\Users\query\AppData\Roaming\Typora\typora-user-images\image-20210917165656350.png)



## 漏洞利用

反弹 shell （不一定成功，因为判断局限很多，且只适用于目标机器为 liunx，懂的~~~）
做好监听 ----------- 自行测试即可

![image-20210917165903978](C:\Users\query\AppData\Roaming\Typora\typora-user-images\image-20210917165903978.png)



编码解码模块 --> 支持有 url 编码/解码、base64 编码/解码、Hex 编码/解码、Unicode 编码/解码， 因为需求是中文与对应编码转换，所以只支持常见的需求。

增加界面对称 --> 添加‘俄罗斯方块’小游戏



![image-20210917165937113](C:\Users\query\AppData\Roaming\Typora\typora-user-images\image-20210917165937113.png)

小游戏

![image-20210917165958281](C:\Users\query\AppData\Roaming\Typora\typora-user-images\image-20210917165958281.png)
