from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):    #TODO:1.what kind of request method is sent, what kind of data is being passed in what's the user sending to banckend
    #return HttpResponse('Home page')  # Yazı yazdırmak için bu kod kullanılıyor 
    return render(request, 'home.html') 
def room(request):
   # return HttpResponse('ROOM')
   return render(request, 'room.html')