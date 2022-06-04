from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('simulation', views.simulation, name="simulation"),
    path('contact', views.contact, name="contact"),
    path('gallery', views.gallery, name="gallery"),
    path("api", views.api, name="api")
]
