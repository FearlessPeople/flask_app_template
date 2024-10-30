# -*- coding: utf-8 -*-


import os
import sys
from datetime import datetime

from loguru import logger

# 创建 logs 目录，如果不存在
if not os.path.exists('logs'):
    os.makedirs('logs')

# 配置日志文件路径
log_file_path = os.path.join('logs', f"{datetime.now().strftime('%Y-%m-%d')}.log")

# 移除 loguru 默认的日志处理器
logger.remove()

# 添加新的日志处理器 - 输出到文件
logger.add(
    log_file_path,
    rotation="00:00",  # 每天午夜创建新文件
    retention="7 days",  # 日志保留7天
    level="DEBUG",  # 设置日志等级
    encoding="utf-8",
    enqueue=True,  # 异步写入文件
    backtrace=True,  # 追溯错误栈
    diagnose=True  # 显示详细的错误信息
)

# 添加新的日志处理器 - 输出到终端
logger.add(
    sink=sys.stdout,
    level="DEBUG",
    colorize=True,  # 彩色输出
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
)
