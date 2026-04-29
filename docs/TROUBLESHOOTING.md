# 常见问题

## 数据库连接失败

请检查：

- MySQL 服务是否已经启动
- 是否已经创建 `booksdb` 数据库
- `DATABASES` 中的用户名、密码、端口是否正确
- 本地 MySQL 是否允许当前用户连接

## 导入 SQL 失败

请确认：

- 数据库字符集建议使用 `utf8mb4`
- SQL 文件是否完整
- 当前 MySQL 用户是否有建表和写入权限
- SQL 文件中的数据库名是否和本地数据库名一致

## `ModuleNotFoundError`

说明依赖没有安装完整。优先执行：

```bash
pip install -r requirements.txt
```

如果仍然缺依赖，请根据报错逐个安装缺失包，例如：

```bash
pip install django pymysql pandas
```

## 页面可以打开但没有图表

请检查：

- 数据库中是否已经导入数据
- 浏览器控制台是否有 JavaScript 报错
- 图表接口是否返回数据
- 静态资源是否正常加载

## 后台无法登录

如果没有管理员账号，执行：

```bash
python manage.py createsuperuser
```

然后访问：

```text
http://127.0.0.1:8000/admin
```

## 迁移命令失败

如果你只是想快速运行项目，优先导入项目提供的 SQL 文件。只有在你修改模型或自定义数据结构时，再考虑执行：

```bash
python manage.py makemigrations
python manage.py migrate
```
