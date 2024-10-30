# -*- coding: utf-8 -*-

# gunicorn_config.py

import multiprocessing

# 绑定的地址和端口
bind = "127.0.0.1:5002"

# 工作进程数，通常是 CPU 核心数的 2-4 倍
workers = multiprocessing.cpu_count() * 2 + 1

# 工作模式（sync, gevent, eventlet 等）
worker_class = "sync"

# 日志配置
accesslog = "logs/gunicorn_access.log"  # 访问日志文件
errorlog = "logs/gunicorn_error.log"  # 错误日志文件
loglevel = "info"  # 日志级别

# 设置进程的超时时间
timeout = 30

# 设置守护进程
daemon = False
