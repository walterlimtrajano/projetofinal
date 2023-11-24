"""
URL configuration for setup project.

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

from Modelo import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.home, name= 'home'),
    path('page1/', v.page1, name='page1'),
    path('home/', v.home, name='home'),
    path('sobreosite/', v.sobreosite, name='sobreosite'),
    path('suporte/', v.suporte, name='suporte'),
    path('page/delete/<int:id>', v.delete, name='delete')
]
