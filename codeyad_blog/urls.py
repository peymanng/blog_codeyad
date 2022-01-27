from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/' , include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.HomeView.as_view() , name='home'),
    path('about-us', views.AboutUsView.as_view() , name='about'),
    path('contact-us', views.ContactUsView.as_view() , name='contact'),
    path('posts/', include('posts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
