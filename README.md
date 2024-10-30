# Flask App项目模板

## 快速开始

1. 下载项目`git clone git@github.com:FearlessPeople/flask_app_template.git`
2. pycharm打开项目, 根据需要新建虚拟环境
4. 安装依赖包`pip install -r requirements.txt`
5. 在本地`MySQL`新建`flask_db`数据库，根据数据库信息修改`config.py`里的链接用户名和密码
6. 本地运行：`run.py`启动项目，服务器运行：`./flask_server.sh start`
7. 接口文档使用flasgger,访问路径http://localhost:5000/apidocs/

## 开发指南

### 增加接口

直接在api包下开发，然后在`app/__init__.py`中注册蓝图即可

### 增加定时任务

在jobs下编写对应定时任务py文件，然后在`conf_scheduler.py`中配置定时规则
