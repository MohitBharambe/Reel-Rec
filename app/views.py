from django.shortcuts import render, redirect
from .forms import CreateUserForm, MovieForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  login
from django.contrib import messages
from .models import Changelog
from .helpers import  recommend, fetch_posters, asyncio

# Home/Landing 
def home(request):
    return render(request, 'index.html')


# Profile/Account 
@login_required()
def profile(request):
    return render(request, 'auth/usrprofile.html')


# Signup
def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signedin')
    elif request.user.is_authenticated:
        return redirect('signedin')
    else:
        form = CreateUserForm()
    return render(request, 'auth/signup.html')

# Recommendations Page
@login_required()
def rrec(request):
    recommendations = []
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            titles = form.cleaned_data['titles']
            recommendations = recommend(titles,num_recommendations=6)
            ids = [rec['id'] for rec in recommendations]
            posters, _ = asyncio.run(fetch_posters(ids))
            for rec in recommendations:
                rec['poster_url'] = posters.get(rec['id'])
    else:
        form = MovieForm()
    return render(request, 'rrec.html',{'recommendations':recommendations})


# FAQ's
def faqs(request):
    return render(request, 'faq.html')

# Changelog/Updates
def changelog(request):
    changelog = Changelog.objects.all().order_by('-date')
    return render(request, 'changelog.html', {'changelog':changelog})

# Contact
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html')


# Custom Error Handlers
# 404
def page_not_found(request, exception):
    return render(request, 'errors/404.html', status=404)
    
# 500
def server_error(request):
    return render(request, 'errors/500.html', status=500)