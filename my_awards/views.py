from django.shortcuts import redirect, render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from my_awards.models import My_projects, Profile, Comments, Rates
from django.contrib.auth.models import User
from .forms import CommentForm, UpdateProfileForm, ProjectFormNew
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):

    all_my_projects = My_projects.all_my_projects()


    return render(request,'welcome.html',{'all_my_projects':all_my_projects})


@login_required(login_url='/accounts/login/')
def profile(request):

    all_my_projects = My_projects.objects.filter(user = request.user)
    return render(request, 'profile.html', {'all_my_projects':all_my_projects})


@login_required(login_url='/accounts/login/')
def my_projects_new(request):
    if request.method=='POST':
        form = ProjectFormNew(request.POST, request.FILES)
        if form.is_valid():
            my_projects = form.save(commit = False)
            my_projects.user = request.user
            my_projects.save()

            return redirect('home')

    else:
        form = ProjectFormNew()
    return render(request, 'project.html',{'form':form})


@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'my_projects' in request.GET and request.GET['my_projects']:
        search_term = request.GET.get('my_projects')
        searched_my_projects = My_projects.search_my_projects(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message':message, 'my_projects':searched_my_projects}) 

    else:
        message = 'you have not entered anything to search'
        return render(request, 'search.html',{'message':message})
        
               






     
         



