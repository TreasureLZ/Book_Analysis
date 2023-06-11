## 项目简介
这次分享图书分析大屏展示系统，界面简洁大气，功能齐全，是不可多得的比较容易的系统，非常适合毕业设计或者课程设计。

本系统基于 **Django+MVT+Mysql** 。涉及技术比较简单，易于理解，适合**PythonWeb初学者**学习使用。

## 技术栈

### 编辑器

PyCharm  2023.1 (旗舰版)

### 前端技术

基础：Html+Css+JavaScript

框架：[BootStrap](https://www.bootcss.com/)+[JQuery](https://jquery.com/)

### 后端技术

Django+爬虫+数据清晰

数据库：MySQL 8.0.26（个人测试使用）

Python版本：3.9.16（个人测试使用）

Django版本：4.2.2（个人测试使用）

## 本地运行

1.下载zip直接解压或安装git后执行克隆命令

```https://github.com/TreasureLZ/Book_Analysis.git```

2.使用 Pycharm 打开项目，配置python编译环境，

**如果不需要爬虫和数据清洗请跳过 4、5步骤，选择执行第6步骤**

3.打开Navicat For Mysql（也就是数据库管理工具），创建booksdb数据库（命令行也可以）

4.如果需要自定义数据，请调用 **reptile.py** 爬虫文件，其中 **max_page** 是每个分类最大采集页数。爬虫结果会写入data.csv文件（如果采集多次记得备份，因为每次调用爬虫会覆盖）

5.爬取数据以后，需要调用 **clean.py** 数据清洗文件才可以存入数据库（需要修改数据库相关的内容）

6.复制**booksdb.sql**中的文件内容运行。（不需要爬虫和数据清洗可以直接执行）

7.修改 **setting.py** 中数据库相关的内容。

8.使用命令启动 Django 项目`` python manage.py runserver``

9.通过浏览器访问系统主页面（包括后台）

* 前台首页：`http://127.0.0.1:8000/`
* 后台首页：`http://127.0.0.1:8000/admin`

## 注意

* 注意 Django 项目启动应该先切入`cd manage.py所在目录`。
* 注意**修改setting.py**中数据库相关的内容。
* 系统中不存在后台管理员账号，可以**使用命令`python manage.py createsuperuser`创建**即可。
* claen.py中的 **create_engine** 需要修改配置数据库信息

## 项目截图

![image](https://github.com/TreasureLZ/Book_Analysis/assets/111034196/e543e4fb-0a6e-41e0-980a-808dcf29fb7f)
