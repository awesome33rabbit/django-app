#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : {{ cookiecutter.author_name }}
# @Email    : {{ cookiecutter.author_email }}
# @Time     : {{ cookiecutter.timestamp }}
# @File     : models.py python3.9
# @Software : PyCharm {{cookiecutter.project_name}}
# @Desc     : TODO

from django.db import models

from .manages import {{cookiecutter.app_name | title}}Manager


class {{cookiecutter.app_name | title}}(models.Model):
    name = models.CharField("{{cookiecutter.app_name | title}}", max_length=32, unique=True)

    objects = {{cookiecutter.app_name | title}}Manager()

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"

    class Meta:
        db_table = "{{cookiecutter.app_name}}"
        verbose_name = "{{cookiecutter.verbose_name}}"
        verbose_name_plural = verbose_name
