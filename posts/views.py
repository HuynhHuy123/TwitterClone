from urllib.request import Request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
def index(request):
    #If the method is Post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
    #If the form is valid
        if form.is_valid():
        #Yes, Save
            form.save()
        #Redirect to 
            return HttpResponseRedirect('/')
        else:
        #No, Show Error
            return HttpResponseRedirect(form.error.as_json())
    posts =Post.objects.all().order_by('-create')[:20]
    #show
    return render(request, 'posts.html', {'posts': posts})

def delete(request, post_id):
    post =Post.objects.get(id= post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
     posts = Post.objects.get(id = post_id)
     if request.method == 'POST':
          form = PostForm(request.POST, request.FILES, instance=posts)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect('/')
          else:
               return HttpResponseRedirect("not valid") 
     return render(request, 'edit.html',{'posts': posts})

    

def like(request, post_id):
    newlikecount = Post.objects.get(id = post_id)
    newlikecount.likecount += 1
    newlikecount.save()
    return HttpResponseRedirect('/')
