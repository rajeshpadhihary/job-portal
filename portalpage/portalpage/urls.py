"""
URL configuration for portalpage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from portal.views import home
from portal.views import error
from portal.views import about
from portal.views import category
from portal.views import contact
from portal.views import job_detail
from portal.views import job_list
from portal.views import testimonial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('error/',error),
    path('about/',about),
    path('category/',category),
    path('contact/',contact),
    path('job-detail/',job_detail),
    path('job-list/',job_list),
    path('testimonial/',testimonial)
]
