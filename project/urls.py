"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from interiordesignapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),

    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('post_index/', views.post_index, name="post_index"),
    path('detalles/<int:id>/',views.detalle_post_index,name="detalles_post_index"),

    path('about_us', views.about_us, name='about_us'),
    
    path('our_services', views.our_services, name='our_services'),
    path('post_project/',views.post_project,name="post_project"),
    path('project_list/', views.project_list,name="project_list"),
    path('details/<int:id>/',views.details_projects,name="details_project"),
    path('faqs', views.faqs, name='faqs'),
    
    path('contact', views.contact, name='contact'),
    
    path('post-job/', views.post_jobopening, name='post_jobopening'),
    path('jobopening_list', views.jobopening_list, name='jobopening_list'),
    
    path('send_email/', views.send_email, name="send_email"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)