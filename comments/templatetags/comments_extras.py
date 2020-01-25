from django import template

from ..forms import CommentForm
from ..models import Comment
'''
这里我们首先导入 template 这个模块，然后实例化了一个 template.Library 类，并将函数 show_recent_posts 装饰为 register.inclusion_tag，这样就告诉 django，这个函数是我们自定义的一个类型为 inclusion_tag 的模板标签。

'''
register = template.Library()

@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post,
    }
@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    comment_list = post.comment_set.all()
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }