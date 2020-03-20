# 夜风随笔博客线上部署
## 下拉代码到本地
```shell script
git clone -b develop v3.0 https://github.com/kali404/Bolg.git
```
## 创建新的虚拟环境
```shell script
mkvirtualenv -p /usr/bin/python3 blog
```
## 安装所需要的python包
```shell script
pip install -r requirements.txt
```
## 登录到你的MySql数据库
```mysql
create database xxx charset=utf8;
# 新建数据库,并制定字符集
```
## 修改配置文件settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # 数据库引擎
        'HOST': '127.0.0.1', # 数据库主机
        'PORT': 3306, # 数据库端口
        'USER': 'yefeng', # 数据库用户名
        'PASSWORD': 'yefengblog', # 数据库用户密码
        'NAME': 'yefeng_blog_db' # 数据库名字
    },
}
```
## 执行数据库迁移命令
```shell script
python manage.py makemigrations
# 生成迁移文件
python manage.py migrate
# 生成数据库表
```
## 创建网站超级管理员
```shell script
python manage.py createsuperuser
# 按照提示完成超级管理员的创建
```
## 注册七牛云
获得key并修改utils下的image_to_qiniu.py
```python
access_key = 'xxxxxxxx'
secret_key = 'xxxx'
bucket_name = 'xxxxx'
```
## 安装uwsgi服务器
```shell script
pip install uwsgi
```
## 安装nginx服务器
```shell script
sudo apt-get install nginx
```
## 新增nginx配置文件/etc/nginx/cond.d/blog.conf
```nginx
server{
    listen 80;
    server_name blog;
    charset UTF-8;
    access_log /root/blogproject/log/access.log;
    error_log /root/blogproject/log/error.log;

    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:8888;
        uwsgi_read_timeout 60;

    }
    location /static {
        add_header Access-Control-Allow-Origin *;
        add_header Access-Control-Allow-Credentials true;
        alias ~/blogproject/static/; # 改成自己的目录

    }
    location /media {
        add_header Access-Control-Allow-Origin *;
        add_header Access-Control-Allow-Credentials true;
        alias ~/blogproject/media/; # 自己的目录
    }
}
```

## 运行
```shell script
uwsgi --ini uwsgi.ini

sudo service nginx restart
```