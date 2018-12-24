from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
posts=[
    {'author':'Satviki',
     'title':'Blog Post 1',
     'content':'First post content',
     'date_posted':'August 27,2018'
     },
    {'author':'Meghana',
     'title':'Blog Post 2',
     'content':'Second post content',
     'date_posted':'August 28,2018'
     }
    ]
    
@login_required
def home(request):
    context={
        'posts':Post.objects.all()
        }
    return render(request,'blog/home.html',context)
@login_required
def about(request):
    return render(request,'blog/about.html',{'title':'About'})
    
