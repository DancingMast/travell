
from django.urls import path,include

from . import views

urlpatterns=[
    path('register', views.register ,name="register"),
    path('signup', views.register ,name="register"),
    path('login', views.login, name="login"),
    path('logout',views.logout,name="logout"),
    path('showpof',views.showpof,name="showpof"),
    path('popacross',views.max_visit,name="popacross")
]