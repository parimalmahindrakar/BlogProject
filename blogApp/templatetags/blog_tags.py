from django import template
from blogApp.models import Post
register = template.Library()


@register.simple_tag
def total_post():
    return Post.objects.count()

# How many posts are there ?


@register.simple_tag
def latest(count=3):
    latest_posts = Post.objects.order_by('-publish')[:count]
    return latest_posts
