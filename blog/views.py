from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return render(request, 'blog/index.html', context={
#         'title': '我的博客首页',
#         'welcome': '欢迎访问我的博客首页'
#     })
import markdown
from django.shortcuts import get_object_or_404, render
import mistune
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
import re
from .models import Post


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    post.body = mistune.html(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})


# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # post.body = markdown.markdown(post.body,
#     #                               extensions=[
#     #                                   'markdown.extensions.extra',
#     #                                   'markdown.extensions.codehilite',
#     #                                   'markdown.extensions.toc',
#     #                               ])
#
#     '''
#     生成TOC目录
#     '''
#
#     md = markdown.Markdown(extensions=[
#         'markdown.extensions.extra',
#         'markdown.extensions.codehilite',
#         # 记得在顶部引入 TocExtension 和 slugify
#         TocExtension(slugify=slugify),
#     ])
#     # _body = markdown.markdown(post.body,
#     #                               extensions=[
#     #                                   'markdown.extensions.extra',
#     #                                   'markdown.extensions.codehilite',
#     #                                   'markdown.extensions.toc',
#     #                               ])
#     post.body = mistune.html(post.body)
#     m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
#     post.toc = m.group(1) if m is not None else ''
#     return render(request, 'blog/detail.html', context={'post': post})


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

