from datetime import date
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Business, HoodUser, Post
from django.shortcuts import redirect, render
from .forms import LoginForm, RegistrationForm,BusinessForm,AddPost,UpdateProfile
from django.contrib.auth import login,authenticate,logout,decorators,hashers
# Create your views here.
def index(request):
  if request.user.is_authenticated:
    return redirect('home')
  return render(request,'hood/index.html')

def logger(request):
  if request.user.is_authenticated:
    return redirect('home')
  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      user = authenticate(username=email, password=password)
      print(user)
      if user is not None:
        login(request,user)
        return redirect('home')
      return render(request, 'hood/login.html', {'form': form,'errors':'email or password is incorrect'})
    return render(request, 'hood/login.html', {'form': form})
  return render(request, 'hood/login.html', {'form': form})



def signer(request):
  form = RegistrationForm()

  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      neighbour = HoodUser(first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],username=form.cleaned_data['email'],password=hashers.make_password(form.cleaned_data['password']),hood=form.cleaned_data['hood'])
      neighbour.save()
      login(request,neighbour)
      return redirect('home')
    return redirect('signer')
  return render(request,'hood/signup.html',{'form':form})


def search(request):
  if 'search' in request.GET and request.GET['search']:
    searchterm = request.GET['search']
    posts = Business.find_business(searchterm)
    if posts:
     context = {'posts': posts, 'heading':f'search results for {searchterm}'}
     return render(request,'hood/results.html', context=context)
    context = {'heading':f'No search results for term {searchterm}'}
    return render(request,'hood/results.html', context=context)
    
@decorators.login_required(login_url="/login")    
def home(request):
  form = BusinessForm()
  buttonMsg = "Add Business"
  form_title = "Add your Business Details"
  title = f"Businesses in Your Home Area-{request.user.hood}"
  posts = Business.objects.all().filter(hood=request.user.hood)
  contacts = Post.objects.all().filter(is_sos=True)
  

  if request.method == 'POST':
    form = BusinessForm(request.POST,request.FILES)
    if form.is_valid():
      biz = Business(user=request.user,hood=form.cleaned_data['hood'],name=form.cleaned_data['name'],email=form.cleaned_data['email'],biz_type=form.cleaned_data['biz_type'],avatar=form.cleaned_data['avatar'])
      print(biz)
      biz.save()
      return HttpResponseRedirect(reverse('home'))
  context = {'form': form, 'buttonMsg': buttonMsg, 'form_title': form_title,'title': title,'posts':posts,'contacts':contacts}
  return render(request,'hood/home.html',context=context)
@decorators.login_required(login_url="/login")
def news(request):
  return render(request,'hood/home.html')

@decorators.login_required(login_url="/login")
def post(request):
  form = AddPost()
  buttonMsg = "Send Message"
  form_title = "Add a message. It will be visible to people in your locality"
  title = "What Your Neighbours are saying"
  posts = Post.objects.all().filter(h=request.user.hood)
  if request.method == 'POST':
    form = AddPost(request.POST)
    if form.is_valid():
      new_post = Post(post=form.cleaned_data['post'], date_posted=date.today(), user=request.user,h=request.user.hood)
      new_post.save()
      return HttpResponseRedirect(reverse('post'))
  context = {'form': form, 'buttonMsg': buttonMsg, 'form_title': form_title,'title': title,'posts':posts}
  return render(request,'hood/home.html',context=context)
  

@decorators.login_required(login_url="/login")
def settings(request):
  form = UpdateProfile()
  form_heading = "Update Your Information"
  if request.method == 'POST':
    form = UpdateProfile(request.POST)
    if form.is_valid():
      user = request.user
      user.msg = form.cleaned_data['msg']
      user.hood = form.cleaned_data['hood']
      user.avatar = form.cleaned_data['avatar']
      user.save()
      return redirect('profile')
    context = {'form':form, 'form_heading':form_heading}
    return render(request,'hood/results.html',context=context)
  context = {'form':form, 'form_heading':form_heading}
  return render(request,'hood/results.html',context=context)

@decorators.login_required(login_url="/login")
def loggout(request):
  logout(request)
  return redirect('index')

@decorators.login_required(login_url="/login")
def profile(request):
  posts = Business.objects.all().filter(user=request.user).order_by('id')
  postss = Post.objects.all().filter(user=request.user).order_by('date_posted')
  
  context = {'posts': posts,'postss': postss}
  return render(request,'hood/prof.html',context=context)

@decorators.login_required(login_url="/login")
def delete(request,item,id):
  if item=="biz":
   biz = Business.objects.get(pk=id)
   Business.delete_business(biz)
  elif item=="post":
    post = Post.objects.get(pk=id)
    post.delete()
  
  return HttpResponseRedirect(reverse('profile'))


  





