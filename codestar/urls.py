from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import setting


urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("blog.urls"), name="blog-urls"),
    path('summernote/', include('django_summernote.urls')),
    
]
urlpatterns += static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)