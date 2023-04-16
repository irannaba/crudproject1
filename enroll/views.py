from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Usertable
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# This Function Will Add new Item and Show All Items
def add_show(request):
 if request.method == 'POST':
  fm = StudentRegistration(request.POST)
  if fm.is_valid():
   nm = fm.cleaned_data['name']
  #  em = fm.cleaned_data['email']
   tk= fm.cleaned_data['task']
   pw = fm.cleaned_data['password']
   reg = Usertable(name=nm, task=tk, password=pw)
   reg.save()
   fm = StudentRegistration()
 else:
  fm = StudentRegistration()
 stud = Usertable.objects.all()
 return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

# This Function will Update/Edit
def update_data(request, id):
 if request.method == 'POST':
  pi = Usertable.objects.get(pk=id)
  fm = StudentRegistration(request.POST, instance=pi)
  if fm.is_valid():
    fm.save()
    return HttpResponseRedirect('/addandshow/')
 else:
  pi = Usertable.objects.get(pk=id)
  fm = StudentRegistration(instance=pi)
 return render(request, 'enroll/updatestudent.html', {'form':fm})

# This Function will Delete
def delete_data(request, id):
 if request.method == 'POST':
  pi = Usertable.objects.get(pk=id)
  pi.delete()
  return HttpResponseRedirect('/addandshow/')




# Signup View Function
def sign_up(request):
 if request.method == "POST":
  fm = SignUpForm(request.POST)
  if fm.is_valid():
   messages.success(request, 'Account Created Successfully !!') 
   fm.save()
 else: 
  fm = SignUpForm()
 return render(request, 'enroll/signup.html', {'form':fm})

# Login View Function
def user_login(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
      fm = AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
        uname = fm.cleaned_data['username']
        upass = fm.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
          login(request, user)
          messages.success(request, 'Logged in successfully !!')
          return HttpResponseRedirect('/addandshow/')
    else: 
      fm = AuthenticationForm()
    return render(request, 'enroll/userlogin.html', {'form':fm})
  else:
    return HttpResponseRedirect('/')

# Profile
def user_profile(request):
  if request.user.is_authenticated:
    return render(request, 'enroll/profile.html', {'name': request.user})
  else:
    return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/login/')