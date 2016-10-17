from django.shortcuts import render
from .models import Posts
# Create your views here.


def index(request):
    print "i m here"
    # get the blog posts that are published
    # print Posts.objects.all()
    # posts = Posts.objects.filter(published=True)
    # print Posts.objects.all()
    # print posts
    posts = Posts.objects.all()
    # now return the rendered template

    return render(request,'list.html', locals())


def post(request, slug):
    print " i m here"
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'post.html', {'post': post})