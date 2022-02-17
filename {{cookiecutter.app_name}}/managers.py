#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : {{ cookiecutter.author_name }}
# @Email    : {{ cookiecutter.author_email }}
# @Time     : {{ cookiecutter.timestamp }}
# @File     : managers.py python3.9
# @Software : PyCharm {{cookiecutter.project_name}}
# @Desc     : TODO

from django.db import models


class {{cookiecutter.app_name | title}}Manager(models.Manager):
    pass
