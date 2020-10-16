from django.urls import path

from . import views
from django.conf.urls import url

#app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>/", views.entry, name="entry"),
    path("newpage", views.new_page, name="new_page"),
    url(r'^getquery/', views.get_query, name="search"),
    url(r'^getcontent/',views.new_page, name="getcontent")  
]
