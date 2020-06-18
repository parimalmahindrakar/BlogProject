from django.shortcuts import render, get_object_or_404
from blogApp.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from .forms import EmailSendForm, CommentsForm
from taggit.models import Tag
# Create your views here.


def post_list_view(request,tag_slug=None):
    post_list = Post.objects.filter(status__iexact="published")
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'blogApp/post_list.html', {'posts': post_list,'tag':tag})


def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True)
    csubmit = False
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            csubmit = True
    form = CommentsForm()
    return render(request, 'blogApp/post_detail.html', {'post': post, 'form': form, 'csubmit': csubmit, 'comments': comments}) 


def mail_send_view(request, id):
    post = get_object_or_404(Post, id=id, status="published")
    sent = False
    if request.method == "POST":
        form = EmailSendForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} ({cd['email']}), recommends you to read \"{post.title}\" !"
            message = "Read post at"+"\n"+f"{post_url}"+"\n\n"+f"{cd['name']}\'s Comments:"+"\n"+f"{cd['comments']}"
            send_mail(subject, message, 'nightfury4653@gmail.com', [cd['to']])
            sent=True
    else:  
        form = EmailSendForm()
    return render(request, 'blogApp/sharebymail.html', {'form': form, 'post': post,'sent':sent})
    

    
