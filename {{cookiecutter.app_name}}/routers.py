#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author   : {{ cookiecutter.author_name }}
# @Email    : {{ cookiecutter.author_email }}
# @Time     : {{ cookiecutter.timestamp }}
# @File     : routers.py python3.9
# @Software : PyCharm {{cookiecutter.project_name}}
# @Desc     : TODO

from utils_pkg.tools.router_tools import execRouterTool

from . import views

urlpatterns = execRouterTool(views)
