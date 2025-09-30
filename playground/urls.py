from . import views
from django.urls import path
# url conf module
urlpatterns=[
    path("hello/",views.hello,name="index")
]