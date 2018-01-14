
from django.shortcuts import render
from django.utils import timezone
from .models import Post, Categories, Posten
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
import requests
from bs4 import BeautifulSoup
from .forms import MailForm, findallForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect




def post_list(request):
    if request.method == 'GET':
        form = MailForm()
        categories = Categories.objects.all()
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 5)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    elif request.method =='POST':
        form = MailForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data['form_email']
            try:
                send_mail('recipient_list','abone olmak istiyorum', form_email, ['tugrulv89@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    return render(request, '../templates/post_list.html', {'posts':posts,
                                                            'categories':categories,
                                                            'form':form})


def post_list_en(request):
    if request.method == 'GET':
        form = MailForm()
        categories = Categories.objects.all()
        post_list = Posten.objects.all()
        paginator = Paginator(post_list, 5)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
    elif request.method =='POST':
        form = MailForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data['form_email']
            try:
                send_mail('recipient_list','abone olmak istiyorum', form_email, ['tugrulv89@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    return render(request, '../templates/post_listen.html', {'posts':posts,
    'categories':categories})




def blog_post_detail(request, slug, categories):
    post = get_object_or_404(Post, slug=slug)
    categorys = Categories.objects.all()
    relateds = Post.objects.filter(categories__name=categories)[:10]
    alloffs = Post.objects.all().order_by('-yar_tarih')[:5]
    return render(request, '../templates/blog_post_detail.html', {'post': post,
                                                                'categorys':categorys,
                                                                'relateds':relateds,
                                                                'alloffs':alloffs})

def categoryviews(request, categories):
    posts = Post.objects.filter(categories__name=categories)
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    pagelists = paginator.get_page(page)
    categories = Categories.objects.all()
    return render(request, '../templates/category.html', {'posts':posts,
                                                            'pagelists':pagelists,
                                                            'categories':categories})


def blog_post_detail_en(request, slug, categories):
    post = get_object_or_404(Post, slug=slug)
    categorys = Categories.objects.all()
    relateds = Posten.objects.filter(categories__name=categories)[:10]
    alloffs = Posten.objects.all().order_by('-yar_tarih')[:5]
    return render(request, '../templates/blog_post_detailen.html', {'post': post,
                                                                'categorys':categorys,
                                                                'relateds':relateds,
                                                                'alloffs':alloffs})

def categoryviews_en(request, categories):
    posts = Posten.objects.filter(categories__name=categories)
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    pagelists = paginator.get_page(page)
    categories = Categories.objects.all()
    return render(request, '../templates/categoryen.html', {'posts':posts,
                                                            'pagelists':pagelists,
                                                            'categories':categories})
