from re import template
from django.shortcuts import render
from .models import posts
from django.views import generic
from django.views.decorators.http import require_GET
from django.http import HttpResponse

# class based views for posts
class postslist(generic.ListView):
    queryset = posts.object.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 4
    
# class based views for each post
class postdetail(generic.DetailView):
    model = posts
    template_name = 'post.html'
