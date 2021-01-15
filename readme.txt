虚拟环境配置
1. cmd 中 pip install pipenv  （安装pipenv）
2. pycharm的Terminal中 pipenv shell  (自动安装虚拟环境)
3. pycharm的Terminal中 pipenv --venv (查看虚拟环境路径)
4.settings-project name-project Interpreter-Systeam Inerperter 添加虚拟环境系统解释器


搭建django项目工程
1.进入到虚拟环境中：
    在terminal中pipenv shell
2.搭建django项目工程：
    django-admin startproject 项目名 .
3.运行django项目工程：
    python manage.py runserver

   专业版启动运行django项目工程：
        点击右上方的add configuration
        点击+号，选择django server
        设置django server名称
        Fix 添加django项目的根路径、settings.py文件

