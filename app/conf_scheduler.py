# -*- coding: utf-8 -*-

SCHEDULED_JOBS = [
    {  # 测试定时任务
        'id': 'job_test',
        'name': '测试定时任务',
        'func': 'app.jobs.job_test:run',
        'args': None,
        'trigger': 'cron',
        'day': '*',
        'hour': '16',
        'minute': 0
    },

]
