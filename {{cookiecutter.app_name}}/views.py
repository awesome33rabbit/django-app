#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : {{ cookiecutter.author_name }}
# @Email    : {{ cookiecutter.author_email }}
# @Time     : {{ cookiecutter.timestamp }}
# @File     : views.py python3.9
# @Software : PyCharm {{cookiecutter.project_name}}
# @Desc     : TODO

from utils_pkg.views.view_set import ModelViewSet

from .serializers import {{cookiecutter.app_name | title}}, {{cookiecutter.app_name | title}}Serializer


class {{cookiecutter.app_name | title}}Views(ModelViewSet):
    queryset = {{cookiecutter.app_name | title}}.objects.all()
    serializer_class = {{cookiecutter.app_name | title}}Serializer
    http_method_names = ["get", "post", "delete"]

    tags = ["{{cookiecutter.app_name|title}}"]
