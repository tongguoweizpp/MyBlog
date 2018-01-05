from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from DjangoUeditor.models import UEditorField
# Create your models here.


class UserProfile(AbstractUser):
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100, verbose_name=u"头像")
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    occupation = models.CharField(max_length=20, verbose_name=u"职业", default="")
    native_place = models.CharField(max_length=10, default=u"", verbose_name=u"籍贯")
    mobile = models.CharField(max_length=11, verbose_name=u"手机号", null=True, blank=True)
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    about_me_data = models.CharField(max_length=500, verbose_name=u"基本资料", default="")
    about_me_education = models.CharField(max_length=500, verbose_name=u"教育经历", default="")
    about_me_work = models.CharField(max_length=500, verbose_name=u"工作经验", default="")
    about_me_evaluation = models.CharField(max_length=500, verbose_name=u"自我点评", default="")
    gender = models.CharField(choices=(("male", u"男"), ("female", u"女")), max_length=6, default="female",
                              verbose_name=u"性别")
    nation = models.CharField(max_length=20, verbose_name=u"民族", default="汉族")
    address = models.CharField(max_length=100, default=u"", verbose_name=u"地址")
    signature = models.CharField(max_length=200, verbose_name=u"个性签名",
                                 default="在博客的搭建上我付出了自己的心血与汗水，这就和人生一样interesting...")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"个人信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class PythonBlog(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"Python博客"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Essay(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"随笔"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField(max_length=30, db_index=True, unique=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = verbose_name
        ordering = ['-add_time']


class Blog(models.Model):
    python_blog = models.ForeignKey(PythonBlog, null=True, blank=True, verbose_name=u"Python博客")
    essay = models.ForeignKey(Essay, null=True, blank=True, verbose_name=u"随笔")
    category = models.CharField(max_length=2, choices=(("bk", u"博客"), ("essay", u"随笔")), default="bk", verbose_name=u"类别")
    name = models.CharField(max_length=6, verbose_name=u"作者", default="童国伟")
    title = models.CharField(max_length=50, verbose_name=u"文章名")
    abstract = models.CharField(verbose_name=u'摘要', max_length=200, blank=True, null=True)
    content = UEditorField(verbose_name=u'文章内容', width=600, height=300, imagePath="blog/ueditor/",
                           filePath="blog/ueditor/", default="")
    image_url = models.CharField(max_length=100, verbose_name=u"图片地址", default="/static/images/default.jpg")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')
    click_nums = models.IntegerField(default=0, verbose_name=u"浏览量")
    comment = models.CharField(max_length=50, verbose_name=u"评论", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"博客文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class MessageBoard(models.Model):
    name = models.CharField(max_length=10, verbose_name=u"姓名")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"地址")
    message = models.CharField(max_length=500, verbose_name=u"留言")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"留言板"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
