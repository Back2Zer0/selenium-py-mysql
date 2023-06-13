
 # 一、引言



## 整体功能描述

本项目主要实现基于mysql和python的selenium网络爬虫爬取淘宝农产品信息的程序。项目能够完成的任务有：

（1）爬取淘宝农产品零售信息，存入本地mysql数据库中
	（2）对数据库中的农产品信息进行增删改查
	（3）将数据库的信息以CSV表格文件形式存储本地
	（4）除了农产品之外还可以爬取淘宝网的其他信息。

 

## 关键技术

库用到了pymysql , webdriver , csv, time 。Pymysql是pycharm中连接mysql数据库，结合pycharm使用的很方便的一个库。Webdriver需要结合一个Chromedriver插件，配置到环境变量来配合chrome浏览器进行网络爬虫。Webdriver最方便的地方就是能以用户的身份正常浏览网页，从而跳过很多反爬机制，直接在接收到的信息中进行爬取。（当然，我们的爬取操作要在合理合法的范围内）

Csv能够将爬取到的信息，包括存储到数据库中的信息以csv表格文件的形式存储到本地。time库主要用到了睡眠函数sleep()，因为chromedriver需要在程序打开chrome浏览器时爬取网页内容，需要chrome浏览器保持唤醒的状态，否则程序运行很快，信息还未爬取完成，浏览器就被关闭了。所以这是时间控制模块。

总的来说，技术上使用了selenium网络爬虫、时间控制模块、以及mysql数据库管理。

# 二、总体设计

## 功能模块的总体设计

![image](https://github.com/Back2Zer0/selenium-py-mysql/blob/master/picture/wps1.jpg) 

代码中用了很多函数实现用户交互，包括爬虫时目标产品信息的输入，对mysql数据库进行操作时的选择等。这样能让功能函数的使用更加灵活，扩展性强。将爬虫模块和数据库模块划分独立，并尽量完善其功能，方便后续信息的爬取和调整，增强程序鲁棒性。并且sql里特意设立了一个summary表，来存储用户操作过的所有信息，并结合csv模块存储本地。

 

## 环境的要求

MySql:

**1.我们需要一个可供项目实验的mysql用户：**

（不建议大家在项目中直接使用root超级管理员账号访问数据库，这样做实在是太危险了。我们可以使用下面的命令创建名为guest的用户并为其授权）

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps2.jpg) 

初始化是这个样子的。

你可以在user后面的'guest'换成你希望的名称，把by后面的单引号内容换成你希望的密码。

 

**2.pycharm连接mysql之前，要完成一些配置，否则会报错并难以运行。**

 

下面是大致配置的示例：

设置 mysql 数据源(连接你的mysql)

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps3.jpg) 

下载所需要的插件

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps4.jpg) 

这里可以看到配置成功了。可以直接操作mysql终端，也可以在pycharm里通过游标对象向数据库服务器发出SQL语句。

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps5.jpg) 

 

**3.初始化主函数模块**

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps6.jpg) 

 

 

主函数模块总览全局，按照用户给出的标志数进行对应的操作，能够接入其他三个模块的api，进行相应模块的操作



**4.爬虫模块**

 

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps7.jpg) 

爬虫模块主要利用selenium，也就是webdriver来唤醒chrome浏览器，从而以浏览器客户端身份得到目标网页服务器传来的信息。

 

**5.数据库模块**

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps8.jpg) 

数据库模块有很多函数是对应mysql的操作语句的。实际上这些函数的内容结构大差不差，都是连接mysql后利用游标向mysql发送指令，指令则是这些函数主要的不同之处。

 

**6.表格文件模块**

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps9.jpg) 

 

 

 

表格模块主要用到了csv库中的csv相关操作，连接mysql后向mysql发送指令，要求其发送过来爬虫爬取淘宝农产品网页得到的数据，从而将这些数据以csv表格文件形式存储到本地。

 

 

## 运行结果和测试

运行测试环境：

1.mysql (测试环境为 mysql 8.0) 

2.pycharm（python 3.10 以上)

3.chrome（谷歌浏览器最佳） 

4.chromedriver (要对应chrome版本) 

5.Windows10（其他环境难以保证正确性）

 

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps10.jpg) 

**开始界面：**

**选择1，爬取农产品信息**

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps11.jpg) 

出现了预设的农产品名称，也可以自己输入其他产品。

这里选择1.茄子

到mysql中查看收集到的茄子销售信息：

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps12.jpg) 

爬取到的数百条茄子的商品名，对应的价格、月销量、商家。

 

—————————————————————————————————

将茄子的销售信息以csv文件形式存储

 

（当前文件夹的文件）

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps13.jpg) 

操作后

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps14.jpg) 

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps15.jpg) 

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps16.jpg) 

 

**删除存储茄子信息的表**

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps17.jpg) 

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps18.jpg) 

 

删除成功。

——————————————————————————————

 

 

操作已有的数据表中的数据

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps19.jpg) 

（以 白菜 表为例）

 

 

**查找一个数据**

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps20.jpg) 

找到了商家为“密水农家”的商铺信息

 

————————————————————————————————

**删除这个数据**

 

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps21.jpg) 

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps22.jpg) 

---



**添加回来这个数据（一次添加两列数据在表中）**

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps23.jpg) 

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps24.jpg) 

加回来了！

**删除一个表**

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps25.jpg) 

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps26.jpg) 

该表不见了！

**结论**

结论：

此项课设让我们对selenium网络爬虫、时间控制模块、以及mysql数据库管理技术有了更加深刻的认识，提高了编程能力。利用爬虫技术和mysql等非常方便、快速的实现了相同的功能，甚至更加可靠。这提醒我们要多多提高技术水平，实现更加丰富的功能。Shelenium爬虫的优越性在于其能以客户端的形式访问网页，得到网页内容，从而能巧妙地绕过很多阻碍。而mysql对爬虫的信息处理又非常方便。两者的结合能极大提高工作效率。

---



# 三、问题描述

1.在程序运行调试的过程中，出现了很多mysql语句的问题。而且这种问题只有在python结合mysql的写法中才会出现。例如利用游标向mysql发送请求时，如果mysql代码中有python变量，mysql会无法识别并报错。这时需要用一些特定的写法来巧妙的避开问题。

示例：mysql插入语句中存在python列表变量res

![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps27.jpg) 

 

2.运行时报了一个错误‘not all arguments converted during string ![img](https://github.com/Back2Zer0/selenium-py-mysq/picture/wps28.jpg)formatting’，以为是数据输入有问题，结果是游标发送命令的execute函数，多写了一个参数。
