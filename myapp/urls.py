from . import views
from django.urls import path, re_path
from myapp.views import help,home,name,number,string,even_odd

urlpatterns = [
    path('index', views.home),
    path('data', views.data),
    path('even_oddd/<int:number>', views.even_oddd),
    # path('even_oddd/', views.even_oddd),
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
    path('jsondata3/', views.Jsondata3),
    path('display/<str:username>/', views.display),
    path('display2/<int:username>/', views.display),
    path('display3/<slug:username>/', views.display),
    # re_path(r'^article/(?P<year>[0-9]{4})/$', views.year),
    # re_path(r"^(?P<year>[0-9]{4})/$", views.year),
    # re_path(r'^usersite/(?P<username>[a-zA-Z0-9]{2,5})/$', views.uservalue),
    # re_path(r"^site1/(?p<username>\w+)/$", views.uservalue),
    # re_path(r"^site2/(?p<username>\d+)/$", views.uservalue),
    path('website2/<int:data>/', views.website),
    path('basee/', views.base),
    path('form/', views.form),
    path('galary/', views.galaxy),
    path('passpe1/',views.passpermiter1),
    path('passpe2/<int:numbe>',views.passpermiter2),
    path('passpe3/',views.passpermiter3),
    path('image/',views.image),
    path('forme1/',views.form1),
    path('forme2/',views.form2),
    path('forme3/',views.form3),
    path('forme4/',views.form4),

]

# handler404 = "myapp.views.handler404"