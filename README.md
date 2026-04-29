# 图书分析大屏展示系统

> 项目状态：LTS 长期维护。当前项目主要保持学习可用、文档清晰和运行问题修复，不再做大规模架构重构。更多数据分析与可视化项目请查看总入口：[Django_Collection](https://github.com/TreasureLZ/Django_Collection)。

## 项目简介

本项目是一个基于 Django 的图书数据分析与可视化系统，围绕图书数据采集、清洗、入库、统计分析、推荐展示和大屏展示，提供一套适合 Python Web 初学者、课程设计和毕业设计参考的完整案例。

项目流程：

```text
图书数据采集 -> 数据清洗 -> MySQL 入库 -> Django 后台管理 -> 前台图表展示 -> 大屏展示
```

## 适合人群

- 正在学习 Python Web / Django 的初学者
- 需要课程设计、毕业设计项目参考的本科或专科学生
- 想学习数据采集、数据清洗、可视化展示完整流程的同学
- 想在已有项目基础上替换数据、扩展图表或改造页面的开发者

## 功能清单

- 用户登录与注册
- 图书数据展示
- 图书价格区间统计
- 不同类别下出版社发行量 Top5
- 图书推荐页面
- 数据可视化大屏
- Django 后台管理
- 图书数据采集与清洗脚本

## 技术栈

| 类型 | 技术 |
| --- | --- |
| 后端 | Python, Django, MVT |
| 数据库 | MySQL |
| 数据处理 | 爬虫, 数据清洗脚本 |
| 前端 | HTML, CSS, JavaScript |
| UI 与交互 | Bootstrap, JQuery |
| 可视化 | ECharts |
| 推荐环境 | Python 3.9.16, Django 4.2.2, MySQL 8.0.26, PyCharm 2023.1 |

## 本地运行

### 1. 克隆项目

```bash
git clone https://github.com/TreasureLZ/Book_Analysis.git
cd Book_Analysis
```

### 2. 安装依赖

建议使用虚拟环境：

```bash
python -m venv .venv
```

Windows 激活：

```powershell
.venv\Scripts\activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

### 3. 创建数据库

在 MySQL 中创建数据库：

```sql
CREATE DATABASE booksdb DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

### 4. 导入数据

如果只想快速运行项目，可以直接导入项目中的 SQL 文件：

```text
booksdb.sql
```

如果想重新采集和清洗数据，再执行：

- `reptile.py`：采集图书数据，其中 `max_page` 表示每个分类最大采集页数。
- `clean.py`：清洗采集结果，生成 `clean_data.csv` 并写入数据库。

重新采集可能覆盖已有数据文件，执行前建议备份 `data.csv` 和 `clean_data.csv`。

### 5. 修改数据库配置

打开：

```text
djangoPreject/djangoPreject/settings.py
```

修改 `DATABASES` 中的数据库名、用户名、密码、主机和端口。

如果执行 `clean.py`，还需要同步修改脚本中的 `create_engine` 数据库连接信息。

### 6. 启动项目

进入 `manage.py` 所在目录：

```bash
cd djangoPreject
python manage.py runserver
```

访问地址：

- 前台首页：`http://127.0.0.1:8000/`
- 后台首页：`http://127.0.0.1:8000/admin`

如果没有后台管理员账号，可以执行：

```bash
python manage.py createsuperuser
```

## 项目截图

#### 登录

![登录](https://github.com/TreasureLZ/Django_Collection/blob/main/Book_Analysis/images/登录.jpg)

#### 注册

![注册](https://github.com/TreasureLZ/Django_Collection/blob/main/Book_Analysis/images/注册.jpg)

#### 首页

![首页](https://github.com/TreasureLZ/Django_Collection/blob/main/Book_Analysis/images/首页.jpg)

#### 价格区间数量统计

![价格区间数量统计](https://github.com/TreasureLZ/Django_Collection/blob/main/Book_Analysis/images/价格区间数量统计.jpg)

#### 不同类别下出版社发行量 Top5

![不同类别下出版社发行量Top5](https://github.com/TreasureLZ/Django_Collection/blob/main/Book_Analysis/images/不同类别下出版社发行量Top5.jpg)

#### 大屏展示

![大屏展示](https://github.com/TreasureLZ/Django_Collection/blob/main/Book_Analysis/images/大屏展示.jpg)

#### 图书推荐

![图书推荐](https://github.com/TreasureLZ/Django_Collection/blob/main/Book_Analysis/images/图书推荐.jpg)

#### 后台管理

![后台管理](https://github.com/TreasureLZ/Django_Collection/blob/main/Book_Analysis/images/后台管理.jpg)

## 二次开发建议

- 将图书数据替换为电影、音乐、课程、商品等同结构数据
- 增加更多统计指标，例如评分分布、价格走势、分类占比
- 增加关键词搜索、分类筛选、价格筛选
- 优化推荐逻辑，加入协同过滤或内容相似度推荐
- 增加数据导出、图表下载、报告生成等功能

## LTS 维护说明

本项目已经进入 LTS 维护阶段，详细说明见 [docs/LTS.md](docs/LTS.md)。

常见运行问题见 [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)。

## 交流

- 总入口：[Django_Collection](https://github.com/TreasureLZ/Django_Collection)
- GitHub 主页：[TreasureLZ](https://github.com/TreasureLZ)

如果项目对你有帮助，欢迎 star 支持。提交 issue 时请尽量附上系统环境、Python 版本、报错截图和复现步骤。
