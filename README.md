
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


![wps1](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/e4d0eed8-976d-46ac-a3c1-311f61a9d8fc)

代码中用了很多函数实现用户交互，包括爬虫时目标产品信息的输入，对mysql数据库进行操作时的选择等。这样能让功能函数的使用更加灵活，扩展性强。将爬虫模块和数据库模块划分独立，并尽量完善其功能，方便后续信息的爬取和调整，增强程序鲁棒性。并且sql里特意设立了一个summary表，来存储用户操作过的所有信息，并结合csv模块存储本地。

 

## 环境的要求

MySql:

**1.我们需要一个可供项目实验的mysql用户：**

（不建议大家在项目中直接使用root超级管理员账号访问数据库，这样做实在是太危险了。我们可以使用下面的命令创建名为guest的用户并为其授权）

![wps2](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/40669898-1bc2-4d43-a092-7af03fc97022)


初始化是这个样子的。

你可以在user后面的'guest'换成你希望的名称，把by后面的单引号内容换成你希望的密码。

 

**2.pycharm连接mysql之前，要完成一些配置，否则会报错并难以运行。**

 

下面是大致配置的示例：

设置 mysql 数据源(连接你的mysql)


![wps3](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/eb36cb7c-619c-49ed-88b8-f7d663fd4dfe)

下载所需要的插件


![wps4](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/d0485275-9c11-4387-99e1-0f05811ec833)

这里可以看到配置成功了。可以直接操作mysql终端，也可以在pycharm里通过游标对象向数据库服务器发出SQL语句。



 ![wps5](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/44585c4b-3487-4d6c-9dae-5530c28fe320)


**3.初始化主函数模块**



 ![wps6](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/213bb83e-2bc3-49d2-81a4-3ee43b67b856)


 

主函数模块总览全局，按照用户给出的标志数进行对应的操作，能够接入其他三个模块的api，进行相应模块的操作



**4.爬虫模块**

 

![wps7](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/88864296-98aa-4a2a-87f7-8bc952ab8c17)


爬虫模块主要利用selenium，也就是webdriver来唤醒chrome浏览器，从而以浏览器客户端身份得到目标网页服务器传来的信息。

 

**5.数据库模块**


![wps8](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/f4789b6d-6206-4029-9261-a8054aed819b)

数据库模块有很多函数是对应mysql的操作语句的。实际上这些函数的内容结构大差不差，都是连接mysql后利用游标向mysql发送指令，指令则是这些函数主要的不同之处。

 

**6.表格文件模块**



 
![wps9](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/fad69ce6-9633-41b0-874c-07ff064917b6)

 

 

表格模块主要用到了csv库中的csv相关操作，连接mysql后向mysql发送指令，要求其发送过来爬虫爬取淘宝农产品网页得到的数据，从而将这些数据以csv表格文件形式存储到本地。

 

 

## 运行结果和测试

运行测试环境：

1.mysql (测试环境为 mysql 8.0) 

2.pycharm（python 3.10 以上)

3.chrome（谷歌浏览器最佳） 

4.chromedriver (要对应chrome版本) 

5.Windows10（其他环境难以保证正确性）

 
![wps10](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/50290a46-79a5-49f8-ad1d-fc750ec4bca3)



**开始界面：**

**选择1，爬取农产品信息**

![wps11](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/99856302-e504-49a8-86c2-38bfd2355b41)


出现了预设的农产品名称，也可以自己输入其他产品。

这里选择1.茄子

到mysql中查看收集到的茄子销售信息：

![wps12](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/a44d4c64-eb2f-4b26-91e0-d044653ab8c7)


爬取到的数百条茄子的商品名，对应的价格、月销量、商家。

 

—————————————————————————————————

将茄子的销售信息以csv文件形式存储

 

（当前文件夹的文件）


![wps13](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/4088be5e-d22d-4907-abdf-9661693b6119)

操作后


![wps14](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/861ad3dd-f35b-4355-9eeb-176c3396fb02)


 ![wps15](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/d3186224-1262-4e89-9512-0cf0d3fa4fa5)

![wps16](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/fe7ac8fa-2f39-4a06-bf5e-207f7ed06700)

**删除存储茄子信息的表**


 

删除成功。

——————————————————————————————

 ![wps17](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/0aac6185-59c2-4388-b6b2-31b25096b2cf)

![wps18](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/aeb8b2a5-78b2-4368-a674-87fbb77bb964)

 

操作已有的数据表中的数据



（以 白菜 表为例）

 

![wps19](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/ba68a1a7-a666-4e61-a2d5-fc413ac0be10)



**查找一个数据**


![wps20](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/93028934-d3f5-4afa-8520-3c860458d8cb)

找到了商家为“密水农家”的商铺信息

 

————————————————————————————————

**删除这个数据**

 

![wps21](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/069169d3-23f5-4504-aee1-52ba2f3fcc0c)


![wps22](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/eb3fac37-d90b-4c35-9762-1159f7d5435f)


---



**添加回来这个数据（一次添加两列数据在表中）**

![wps23](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/ed3fca4a-ea93-4216-85fe-5ad87527d3f9)

![wps24](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/b9a87383-8852-4d02-900a-2d33c2bde8bf)

加回来了！

**删除一个表**
![wps25](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/0f30750b-bea6-43a3-b185-78334984915c)

![wps26](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/84e7d35b-7f5b-419d-9dbc-96a8920b1e73)


该表不见了！

**结论**

结论：

此项课设让我们对selenium网络爬虫、时间控制模块、以及mysql数据库管理技术有了更加深刻的认识，提高了编程能力。利用爬虫技术和mysql等非常方便、快速的实现了相同的功能，甚至更加可靠。这提醒我们要多多提高技术水平，实现更加丰富的功能。Shelenium爬虫的优越性在于其能以客户端的形式访问网页，得到网页内容，从而能巧妙地绕过很多阻碍。而mysql对爬虫的信息处理又非常方便。两者的结合能极大提高工作效率。

---



# 三、问题描述

1.在程序运行调试的过程中，出现了很多mysql语句的问题。而且这种问题只有在python结合mysql的写法中才会出现。例如利用游标向mysql发送请求时，如果mysql代码中有python变量，mysql会无法识别并报错。这时需要用一些特定的写法来巧妙的避开问题。

示例：mysql插入语句中存在python列表变量res



 ![wps27](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/95fd9892-db04-46d0-9701-01f14e14cb62)


2.运行时报了一个错误‘not all arguments converted during string formatting’，以为是数据输入有问题，结果是游标发送命令的execute函数，多写了一个参数。

![wps28](https://github.com/Back2Zer0/selenium-py-mysql/assets/101703195/7846be99-b41c-4102-a917-0e231dd67d64)

