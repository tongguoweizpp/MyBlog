"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve

from MyBlog.settings import MEDIA_ROOT, STATIC_ROOT
import xadmin
from users.views import MessageView, AboutMeView, EssayView, PythonBlogView, IndexView, DetailView
from users.views import savemessage

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    # 首页url
    url(r'^$', IndexView.as_view(), name="index"),

    # 关于我url
    url(r'^about_me/$', AboutMeView.as_view(), name="about_me"),
    # python博客url
    url(r'^python_blog/$', PythonBlogView.as_view(), name="python_blog"),
    # 随笔url
    url(r'^essay/$', EssayView.as_view(), name="essay"),
    # 详情url
    url(r'^detail/(?P<python_blog_id>\d+)/$', DetailView.as_view(), name="detail"),
    # 留言板url
    url(r'^message/$', MessageView.as_view(), name="message"),
    # 留言保存url
    url(r'^savemessage/$', savemessage, name="savemessage"),

    # 配置静态文件url
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    # 富文本编辑器配置url
    url(r'^ueditor/', include('DjangoUeditor.urls')),
]


# 全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
