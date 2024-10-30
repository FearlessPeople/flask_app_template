#!/bin/bash

# 获取当前脚本所在目录的绝对路径
APP_DIR="$(cd "$(dirname "$0")"; pwd)"

# 激活虚拟环境
source "$APP_DIR/venv/bin/activate"

# 定义其他变量
APP_NAME="flask_app"  # 应用名称
GUNICORN="gunicorn"  # Gunicorn 命令
USER="$(whoami)"  # 运行的用户
PID_FILE="$APP_DIR/gunicorn.pid"  # Gunicorn PID 文件
CONFIG_FILE="$APP_DIR/gunicorn_config.py"  # Gunicorn 配置文件路径

# 启动函数
start() {
    echo "Starting $APP_NAME..."
    cd $APP_DIR
    $GUNICORN -c $CONFIG_FILE run:app --pid $PID_FILE --daemon
    echo "$APP_NAME started."
}

# 停止函数
stop() {
    if [ -f $PID_FILE ]; then
        echo "Stopping $APP_NAME..."
        kill $(cat $PID_FILE)
        rm $PID_FILE
        echo "$APP_NAME stopped."
    else
        echo "$APP_NAME is not running."
    fi
}

# 重启函数
restart() {
    stop
    start
}

# 状态函数
status() {
    if [ -f $PID_FILE ]; then
        echo "$APP_NAME is running with PID $(cat $PID_FILE)."
    else
        echo "$APP_NAME is not running."
    fi
}

# 处理传入的命令
case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    status)
        status
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
esac

exit 0
