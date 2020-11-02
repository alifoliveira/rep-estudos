from django.shortcuts import render

# Create your views here.

def feed(request):
    context = {}
    return render(request, 'main/feed.html', context)

def post(request):
    return render(request, 'main/post.html')

