from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import PostForm

from .models import NewPost

# Create your views here.

def feed(request):
    allposts = NewPost.objects.all().order_by('-created_at')
    return render(request, 'app/feed.html', {'posts':allposts})

def newpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()
        return render(request, 'app/newpost.html', {'form':form})

def editpost(request, id):
    post = get_object_or_404(NewPost, pk=id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect('/')
        else:
            return render(request, 'app/editpost.html', {'form':form, 'post':post})
    else:
        return render(request, 'app/editpost.html', {'form':form, 'post':post})

def deletepost(request, id):
    post = get_object_or_404(NewPost, pk=id)
    post.delete()
    
    messages.info(request, 'Post Successful deleted.')
    
    return redirect('/')

def about(request):
    return render(request, 'app/about.html')
