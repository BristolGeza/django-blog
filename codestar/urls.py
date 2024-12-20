from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
]

#from django.contrib import admin
#from django.urls import path, include

#urlpatterns[

   # path("", include("blog.urls"), name="blog-urls"),
    #path('admin/', admin.site.urls,)
#]