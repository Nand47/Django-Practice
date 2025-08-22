from . import views
from django.urls import path, re_path
from myapp.views import help,home,name,number,string,even_odd

urlpatterns = [
    path('index', views.home),
    path('data', views.data),
    # path('even_odd/<int:number>', views.even_odd),
    path('even_odd', views.even_odd),
    path('html/', views.htmlfile),
    path('data_file/', views.datafile),
    path('homee/',home),
    path('help/',help),
    path('user/<name>/', name),
    path('number/<int:number>/', number),
    path('string/<str:string>/', string),
    path('even_odd/<int:num>/', even_odd),
    path('jsondata/', views.Jsondata),
    path('jsondata2/', views.Jsondata2),
    # path('jsondata3/', views.Jsondata3),
    # path('display/<str:username>/', views.display),
    # path('display2/<int:username>/', views.display),
    # path('display3/<slug:username>/', views.display),
    # re_path(r'^article/(?P<year>[0-9]{4})/$', views.year),
    # re_path(r"^(?P<year>[0-9]{4})/$", views.year),
    # re_path(r'^usersite/(?P<username>[a-zA-Z0-9]{2,5})/$', views.uservalue),
    # re_path(r"^site1/(?p<username>\w+)/$", views.uservalue),
    # re_path(r"^site2/(?p<username>\d+)/$", views.uservalue),
    # path('website2/<int:data>/', views.website),
    path('basee/', views.base),
    path('form/', views.form),
    path('galary/', views.galaxy)
]

# handler404 = "myapp.views.handler404"