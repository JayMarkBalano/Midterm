from tempfile import template
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class BlogListView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'app/blog_list.html'

class BlogDetailView(DetailView):
    model = BlogPost
    context_object_name = 'post'  # fixed spelling
    template_name = 'app/blog_detail.html'

class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'author', 'content', 'category', 'image']  # updated fields
    template_name = 'app/blog_create.html'
    success_url = reverse_lazy('blog')

class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'author', 'content', 'category', 'image']
    template_name = 'app/blog_update.html'
    success_url = reverse_lazy('blog')

class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'app/blog_delete.html'
    success_url = reverse_lazy('blog')