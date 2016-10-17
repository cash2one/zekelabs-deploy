from django.shortcuts import render

from django.forms import inlineformset_factory
from .models import RegisterProfile,Courses, Event, SubjectMatterExpert
from .forms import Register, RegisterCourse
 #,ImageForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.views.generic import DetailView, TemplateView
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory

from mezzanine.blog.models import BlogPost
from django.db.models import Q
# Create your views here.

def register_generic(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            form.save()
            from_email = 'zekelabs@gmail.com'
            msg = EmailMultiAlternatives(subject, 'From ' + mobile + ' ' + email + ' ' + message, from_email, ['zekelabs@gmail.com'])
            msg.send()        
            return render(request,'done.html',locals())
        return render(request,'notdone.html',locals())
    else:
        form = Register()
    return render(request,'register.html',locals())   


def register(request,slug = None):
    subject = slug 
    print subject
    if request.method == 'POST':
        form = RegisterCourse(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            message = form.cleaned_data['message']
            print subject 
            form.save()
            from_email = 'zekelabs@gmail.com'
            msg = EmailMultiAlternatives(subject, 'From ' + mobile + ' ' + email + ' ' + message, from_email, ['zekelabs@gmail.com'])
            msg.send()        
            return render(request,'done.html',locals())
        return render(request,'notdone.html',locals())
    else:
        form = RegisterCourse()
    return render(request,'register.html',locals())   

def register_event(request,slug = None):
    subject = slug
    print subject
    if request.method == 'POST':
        form = RegisterCourse(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            couponcode = form.cleaned_data['message']
            print couponcode
            form.save()
            from_email = 'zekelabs@gmail.com'
            msg = EmailMultiAlternatives(subject, 'From ' + mobile + ' ' + email + ' ' + couponcode, from_email, ['zekelabs@gmail.com'])
            msg.send()
            return render(request,'done.html',locals())
        return render(request,'notdone.html',locals())
    else:
        form = RegisterCourse()
    return render(request,'register.html',locals())


def course_detail(request,course): 
    course = Courses.objects.filter(slug=course)
    return render(request, 'course_detail.html', locals()) 

def show_webinars(request):
    events = Event.objects.all()
    return render(request, 'events.html', locals())
    
def get_webinar(request,slug):
    print slug
    data = Event.objects.get(slug=slug)
    return render(request, 'webinar.html', locals())
   
def show_smes(request):
    smes = SubjectMatterExpert.objects.all()
    return render(request, 'sme.html', locals())


def show_blogs(request):
    blogs = BlogPost.objects.all()
    return render(request, 'kbytes.html', locals())
 
def show_blog(request,slug):
    print slug
    blog = BlogPost.objects.get(id=slug)
    return render(request, 'kbyte.html', locals())
 
def searchtag_blogs(request,slug = None):
    if request.GET:
       slug = request.GET["item"]
    if slug:
       blogs = BlogPost.objects.filter( Q(title__icontains=slug)| Q(content__icontains=slug))
    else:
       blogs = None
    return render(request, 'search.html', locals())
 
def show_blog_by_slug(request,slug):
    print slug
    blog = BlogPost.objects.get(slug=slug)
    return render(request, 'kbyte.html', locals())
 
def search_courses(request,slug = None):
    if request.GET:
       slug = request.GET["item"]
    if slug:
       courses = Courses.objects.filter( Q(title__icontains=slug)| Q(overview__icontains=slug))
    else:
       courses = None
    return render(request, 'search-courses.html', locals())

def academia(request):
    return render(request,'academia.html', locals())

def aboutus(request):
    return render(request,'aboutus.html', locals()) 

def termsandcondition(request):
    return render(request,'termsandcondition.html', locals())

