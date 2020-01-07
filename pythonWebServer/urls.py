"""pythonWebServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from urlapp import views
from teststaticapp import views as v

from django.conf.urls.static import static
from django.conf import settings
from validformapp import views as fv

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("user/<int:month>/<int:year>/", views.home, name="home"),
                  path("test/", include("urlapp.test")),
                  path("about/", views.about, name="about"),
                  path("stat/", v.home, name="static"),
                  path("pizza/<int:pizza_id>", v.pizza_detail, name="pizza_detail"),
                  path("formpage/", fv.form_page, name="form-page")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
