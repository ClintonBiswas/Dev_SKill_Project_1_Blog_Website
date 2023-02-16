from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Blog, Category, Likes
from django.contrib.auth.decorators import login_required
from .forms import BlogAddForm, BlogComment
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.

def Home(request):
    blog = Blog.objects.all()
    # blog_count = Blog.objects.all().filter(category='Personal blogs')
    # print(blog_count)
    category_list = Category.objects.all()
    dict = {'blogs': blog, 'category_list': category_list}
    return render(request, 'Blog/home.html', context=dict)

def CategoryBlogs(request, pk):
    category = Category.objects.get(pk=pk)
    #print(category)
    blog_list = Blog.objects.filter(category=category)
    #print(blog_list)
    dict = {'blog_list':blog_list, 'category': category}
    return render(request, 'Blog/category_blog.html',context=dict)

# checking Custom Forms
# @login_required
# def BlogFormView(request):
#     category_list = Category.objects.all()
#     form = BlogAddForm()
#     if request.method == 'POST':
#         form = BlogAddForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = get_object_or_404(User, pk=request.user.pk)
#             category = get_object_or_404(Category, pk=request.POST['category'])
#             blog = form.save(commit=False)
#             blog.user = user
#             blog.category = category
#             blog.save()
#             return redirect('blog:home')
#         else:
#             print(form.errors)

#     dict={'category_list':category_list, 'form':form}
#     return render(request, 'Blog/blog_form.html', context=dict)

@login_required
def BlogFormView(request):
    form = BlogAddForm()
    if request.method == "POST":
        form = BlogAddForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            blog = form.save(commit=False)
            blog.user = user
            print(blog.user)
            blog.save()
            return redirect('blog:home')
    dict={'form':form}
    return render(request, 'Blog/blog_form.html', context=dict)

@login_required
def BlogDetails(request, slug):
    blog = Blog.objects.get(slug=slug)
    blog_list = Blog.objects.order_by('created')
    already_liked = Likes.objects.filter(blog=blog, user= request.user)
    if already_liked:
        liked = True
    else:
        liked = False
    form = BlogComment()
    #print(blog_list)
    if request.method == 'POST':
        form = BlogComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('blog:blog_details', kwargs={'slug':slug}))
    dict={'blog':blog, 'blog_list': blog_list, 'form':form, 'liked':liked,}
    return render(request, 'Blog/blog_details.html', context=dict)