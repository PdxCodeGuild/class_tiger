# Import django and models

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from chirprprofile.forms import SignupForm, SigninForm
from chirps.forms import ChirpForm 

# Views

def profile(request, username):
  if request.user.is_authenticated:
    user = User.objects.get(username=username)
    
    if request.method == 'POST':
      form = ChirpForm(data=request.POST)

      if form.is_valid():
        chirp = form.save(commit=False)
        chirp.user = request.user
        chirp.save()
        
        redirecturl = request.POST.get('redirect', '/')

        return redirect(redirecturl)
    else:
      form = ChirpForm()

    return render(request, 'profile.html', {'form': form, 'user': user})
  else:
    return redirect('/')

def frontpage(request):
  if request.user.is_authenticated:
    return redirect('/' + request.user.username + '/') # Change this line
  else:
    if request.method == 'POST':
      if 'signupform' in request.POST:
        signupform = SignupForm(data=request.POST)
        signinform = SigninForm()
        
        if signupform.is_valid():
          username = signupform.cleaned_data['username']
          password = signupform.cleaned_data['password1']
          signupform.save()
          user = authenticate(username=username, password=password)
          login(request, user)
          return redirect('/')
      else:
        signinform = SigninForm(data=request.POST)
        signupform = SignupForm()
        
        if signupform.is_valid():
          login(request, signupform.get_user())
          return redirect('/')
    else:
      signupform = SignupForm()
      signinform = SigninForm()
  
    return render(request, 'frontpage.html', {'signupform': signupform, 'signinform': signinform})

def signout(request):
  logout(request)
  return redirect('/')

# add followers

def follows(request, username):
    # call an instance of User  and add a follows attribute
  user = User.objects.get(username=username)
  chirprprofiles = user.chirprprofile.follows.select_related('user').all()
    
  return render(request, 'users.html', {'title': 'Follows', 'chirprprofiles': chirprprofiles})
  
def followers(request, username):
     # call an instance of User  and add a follows attribute
  user = User.objects.get(username=username)
  chirprprofiles = user.chirprprofile.followed_by.select_related('user').all()
    
  return render(request, 'users.html', {'title': 'Followers', 'chirprprofiles': chirprprofiles})

# @login_required decorator so that if you try to go to a view
#  you'll be sent to the sign in page.
@login_required
def follow(request, username):
  user = User.objects.get(username=username)
  request.user.chirprprofile.follows.add(user.chirprprofile)
  
  return redirect('/' + user.username + '/')

@login_required
def stopfollow(request, username):
  user = User.objects.get(username=username)
  request.user.chirprprofile.follows.delete(user.chirprprofile)
  
  return redirect('/' + user.username + '/')  