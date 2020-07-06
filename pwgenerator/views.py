from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'pwgenerator/home.html')

# Password page view
def password(request):

    # Starting list of lower case characters for random password
    characters = list('abcdefghijklmnopqrstuvwxyz')

    # Form inputs
    # add uppercase characters to the characters list if selected
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # add special characters if selected
    if request.GET.get('special'):
        characters.extend(list('!@#$%&*'))

    # add numbers if selected
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    # length of the password, default length of 12 if nothing chosen
    length = int(request.GET.get('length', 12))

    # loop through the 'characters' list to pick a random characer from the list and add it to
    # 'the_password' variable, the number of 'length' times
    the_password = ''
    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'pwgenerator/password.html', {'password': the_password})

# About page view
def about(request):
    return render(request, 'pwgenerator/about.html')
