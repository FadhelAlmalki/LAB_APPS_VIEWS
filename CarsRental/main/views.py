from django.shortcuts import render
import random
import string

def home_view(request):

    return render(request,'main/home.html')

def about_view(request):

    return render(request, 'main/about.html')

def password_generator_view(request):
    
    length = 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    return render(request, 'main/password_generator.html', {'password': password})


