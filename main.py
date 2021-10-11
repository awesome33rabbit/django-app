#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : PMZ
# @Email    : pumz_1991@126.com
# @Time     : 2021/10/11 15:40
# @File     : main.py python3.9
# @Software : PyCharm django-app
# @Desc     : TODO

from datetime import datetime

from cookiecutter.main import cookiecutter

if __name__ == "__main__":
    cookiecutter(
        "https://github.com/awesome33rabbit/django-app.git",
        extra_context={"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
    )
