import datetime

from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.http import urlencode



def navia_home(request):
    return render(request, 'navia_home/navia_home.html')