#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : PMZ
# @Email    : pumz_1991@126.com
# @Time     : 2021/10/13 12:14
# @File     : local.py python3.9
# @Software : PyCharm django-app
# @Desc     : TODO

from datetime import datetime

from cookiecutter.main import cookiecutter

if __name__ == "__main__":
    cookiecutter(
        ".", extra_context={"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    )
