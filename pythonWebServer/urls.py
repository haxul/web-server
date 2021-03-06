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
from authapp import views as av
from django.contrib.auth import views as auth_views
from authapp import views as main_views
from firstapp import apis
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/auth/', include('rest_framework_social_oauth2.urls')),
                  path("python/", main_views.main_page, name="main_page"),
                  path("user/<int:month>/<int:year>/", views.home, name="home"),
                  path("test/", include("urlapp.test")),
                  path("about/", views.about, name="about"),
                  path("stat/", v.home, name="static"),
                  path("pizza/<int:pizza_id>", v.pizza_detail, name="pizza_detail"),
                  path("formpage/", fv.form_page, name="form-page"),
                  path("", av.home, name="main"),
                  path("authapp/login/", auth_views.LoginView.as_view(template_name="authapp/login.html", ),
                       name="login"),
                  path("/", auth_views.LogoutView.as_view(),
                       name="logout"),
                  path("authapp/signup/", main_views.sign_up, name="sign_up"),
                  path("api/client/pizzashops", apis.client_get_pizzashops),
                  path("api/<int:pizzashop_id>/pizzas", apis.get_pizzas)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


