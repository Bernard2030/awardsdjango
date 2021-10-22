from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from my_awards.models import My_projects

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




     
         



