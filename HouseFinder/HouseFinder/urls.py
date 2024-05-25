"""
URL configuration for HouseFinder project.

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
from django.conf import settings
from houseFinderApp.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',index,name='index'),
    path('house_signup/',house_signup,name='house_signup'),
    path('house_login/',house_login,name='house_login'),
    path('post_success/',post_success,name='post_success'),
    path('post/',post,name='post'),
    path('product_page/<id>/',product_page,name='product_page'),
    path('profile1/<id>/',profile1,name='profile1'),
    path('logout_page/',logout_page,name='logout_page'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()