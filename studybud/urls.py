"""studybud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include  #7.inlude -> base urls'den haberdar olabilmesi için önemlidir.
#from django.http import HttpResponse  # 2. actually going to render a template yet , it will be from  (Burası Silindi)
 
 
#def home(request):    #TODO:1.what kind of request method is sent, what kind of data is being passed in what's the user sending to backend
 #   return HttpResponse('Home page')  # Yazı yazdırmak için bu kod kullanılıyor 

#def room(request):
 #   return HttpResponse('ROOM')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home),    # 3.Artık url e giriyruz , biri home page e gitti Home -> fonksiyonu tetiklicek (Silindi)
    #path('room/', room) # 'room/' bu komut çağırma gibi bir şey  (silindi)
    path('', include('base.urls'))

]
