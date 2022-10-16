#4.Burayı studybud urls.py dosyasını tanımlayabilmek için yaptık 

from django.urls import path #5.kesin gerekli  !! View.py ile aynı dosyada olması gerekiyor
from . import views as lahmacun # as -> bir isim tanımlama gibi düşün lahamcun diyince views i çağıaracak. 

urlpatterns = [                               #6.
    path('', lahmacun.home, name="home"),
    path('room/', lahmacun.room, name="room"),
]
