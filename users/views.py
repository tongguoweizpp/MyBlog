from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import UserProfile, Blog, MessageBoard
# Create your views here.


def savemessage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message = request.POST.get('message')

        when_message = MessageBoard.objects.filter(message=message)
        if when_message:
                return
        else:
            visitor_message = MessageBoard()
            visitor_message.name = name
            visitor_message.email = email
            visitor_message.address = address
            visitor_message.message = message
            visitor_message.save()
    return render(request, 'message.html', {})


class MessageView(View):
    def get(self, request):
        # 选出随笔文章并按点击量排序
        all_messages = MessageBoard.objects.all().order_by("-add_time")
        # 个人资料
        all_profiles = UserProfile.objects.all()
        return render(request, 'message.html', {
            'all_messages': all_messages,
            'all_profiles': all_profiles,
        })


class AboutMeView(View):
    def get(self, request):
        all_aboutmes = UserProfile.objects.all()
        # 个人资料
        all_profiles = UserProfile.objects.all()
        return render(request, 'about-me.html', {
            'all_aboutmes': all_aboutmes,
            'all_profiles': all_profiles,
        })


class EssayView(View):
    def get(self, request):
        # 选出随笔文章并按点击量排序
        all_essays = Blog.objects.filter(category="sb").order_by("-click_nums")
        # 随笔文章按添加时间排序
        all_sbs = Blog.objects.filter(category="sb").order_by("-add_time")

        # 随笔搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_sbs = all_sbs.filter(
                Q(name__icontains=search_keywords) |
                Q(category__icontains=search_keywords) |
                Q(title__icontains=search_keywords) |
                Q(content__icontains=search_keywords) |
                Q(tags__icontains=search_keywords)
            )

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_sbs, 5, request=request)

        sbs = p.page(page)

        # 个人资料
        all_profiles = UserProfile.objects.all()
        return render(request, 'essay.html', {
            'all_essays': all_essays,
            'all_sbs': sbs,
            'all_profiles': all_profiles,
        })


class PythonBlogView(View):
    def get(self, request):
        # 选出博客文章并按点击量排序
        all_blogs = Blog.objects.filter(category="bk").order_by("-click_nums")
        # 博客文章按添加时间排序
        all_bks = Blog.objects.filter(category="bk").order_by("-add_time")

        # 随笔搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_bks = all_bks.filter(
                Q(name__icontains=search_keywords) |
                Q(category__icontains=search_keywords) |
                Q(title__icontains=search_keywords) |
                Q(content__icontains=search_keywords) |
                Q(tags__icontains=search_keywords)
            )

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_bks, 5, request=request)

        bks = p.page(page)

        # 个人资料
        all_profiles = UserProfile.objects.all()
        return render(request, 'python-blog.html', {
            'all_blogs': all_blogs,
            'all_bks': bks,
            'all_profiles': all_profiles,
        })


class IndexView(View):
    def get(self, request):
        # 选出博客文章并按时间排序
        all_articles = Blog.objects.all().order_by("-add_time")
        # 选出博客文章并按点击量排序
        all_sorteds = Blog.objects.all().order_by("-click_nums")[:10]
        # 个人资料
        all_profiles = UserProfile.objects.all()
        return render(request, 'index.html', {
            'all_articles': all_articles,
            'all_sorteds': all_sorteds,
            'all_profiles': all_profiles,
        })


class DetailView(View):
    def get(self, request, python_blog_id):
        # 选出博客文章并按点击量排序
        blog = Blog.objects.get(id=int(python_blog_id))
        # 增加点击数
        blog.click_nums += 1
        blog.save()
        # 个人资料
        all_profiles = UserProfile.objects.all()
        return render(request, 'detail.html', {
            'blog': blog,
            'all_profiles': all_profiles,
        })


def page_not_found(request):
    # 404处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    # 500处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response
