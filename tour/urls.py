
from django.urls import path,include

from . import views

urlpatterns=[
    path('',views.realhome,name="realhome"),
    path('getstart',views.home,name="home"),
    path('cat1',views.cat,name="cat"),
    path('cat2',views.catmon,name="catmon"),
    path('cat3',views.sect,name="sect"),
    path('cat4',views.predict,name="sect"),
    path('cat5',views.regret,name="regret"),
    path('dashbut',views.dash,name="dash"),
    path('homebut',views.realhome,name="home1"),
    path('abobut',views.realhome,name="abobut"),
    path('setdata',views.setdata,name="setdata"),
    # path('regraph',views.predict,name="regraph"),
]