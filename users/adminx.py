# -*- coding:utf-8 -*-
__author__ = 'tgw'
__date__ = '2017/12/10 16:37'
import xadmin

from xadmin import views
from .models import Banner, Tag, Blog, PythonBlog, Essay, MessageBoard


class BaseSetting(object):
    """
    启用xadmin的主题功能
    """
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    """
    修改xadmin的左上角名称，底部名称, 收起app
    """
    site_title = "童国伟的博客后台"
    site_footer = "童国伟的博客"
    menu_style = "accordion"


class BannerAdmin(object):
    list_display = ["title", "image", "url", "index", "add_time"]
    search_fields = ["title", "image", "url", "index"]
    list_filter = ["title", "image", "url", "index", "add_time"]


class TagAdmin(object):
    list_display = ["tag", "add_time"]
    search_fields = ["tag"]
    list_filter = ["tag", "add_time"]


class PythonBlogAdmin(object):
    list_display = ["name", "add_time"]
    search_fields = ["name"]
    list_filter = ["name", "add_time"]


class EssayAdmin(object):
    list_display = ["name", "add_time"]
    search_fields = ["name"]
    list_filter = ["name", "add_time"]


class BlogAdmin(object):
    list_display = ["python_blog", "essay", "title", "abstract", "content", "image_url", "tags", "click_nums", "add_time"]
    search_fields = ["python_blog", "essay", "title", "abstract", "content", "image_url", "tags", "click_nums"]
    list_filter = ["python_blog", "essay", "title", "abstract", "content", "image_url", "tags", "click_nums", "add_time"]
    style_fields = {"content": "ueditor"}


class MessageBoardAdmin(object):
    list_display = ["name", "email", "address", "message", "add_time"]
    search_fields = ["name", "email", "address", "message"]
    list_filter = ["name", "email", "address", "message", "add_time"]


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(PythonBlog, PythonBlogAdmin)
xadmin.site.register(Essay, EssayAdmin)
xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(MessageBoard, MessageBoardAdmin)
# 启用xadmin的主题功能的注册
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 修改xadmin的左上角和底部名称的注册
xadmin.site.register(views.CommAdminView, GlobalSettings)
