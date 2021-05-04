from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from.models import Post


# Create your views here.
class BlogListView(List):
    model = Post
    template.name = 'base.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields =['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields =['title', 'body']


class BlogDeleteView(Deleteview):
    model = Post
    template_name ="post_delete.html"
    sucess_url = reverse_lazy('home')