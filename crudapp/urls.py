
from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home page'),
    path('save', views.save, name = 'save page'),
    path('delete', views.delete, name = 'delete page'),
    path('edit', views.edit, name = 'edit page'),
    path('recordedited', views.recordedited, name = 'edit page'),
]
