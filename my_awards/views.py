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

@login_required(login_url='/accounts/login/')
def comment(request,id):
    id=id
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = request.user
            my_projects = My_projects.objects.get(id=id)
            comment.my_projects_id = my_projects
            comment.save()
            return redirect('home')

        else:
            my_projects_id = id
            messages.information(request, 'fill all the fields')
            return redirect ('comment',id = my_projects_id)

    else:
        id = id
        form = CommentForm()
        return render(request, 'comment.html',{'form':form, 'id':id})


@login_required(login_url='/accounts/login/')
def rates(request,id):
    if request.method == 'POST':
        rates = Rates.objects.filter(id = id)
        for rates in rates:
            if rates.user == request.user:
                messages.information(request,'you only rate once')
                return redirect('singleproject',id)

            else:
                messages.information(request,'Input all fields')
                return redirect('singleproject', id)

        else:
            messages.information(request, 'Input all fields')
            return redirect('singleproject', id) 



@login_required(login_url='/accounts/login/')
def logout_request(request):
    """
    The function logs out user
    """                       

    logout(request)
    return redirect('home')



@login_required(login_url='/accounts/login/')
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')

        else:
            form = UpdateProfileForm(request.POST,request.FILES)
            return render(request,'update_profile.html',{'form':form})
                    



    










     
         



