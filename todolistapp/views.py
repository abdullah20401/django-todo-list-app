from django.shortcuts import render

from .models import Todo

# Create your views here.
def home(request):
    context = {'todo': Todo}
    
    return render(request, 'todolistapp/home.html', context)