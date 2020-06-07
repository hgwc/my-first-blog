"""mysite URL Configuration

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
"""
이렇게 사용해도 되고, 아래처럼 사용해도 된다.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
"""

from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
  #  url(r'^accounts/login/$', views.login, name='login'),
    # 위의 문장을 아래처럼 수정하니, 로그인 창이 생성됨
    url( r'^accounts/login/$',views.LoginView.as_view(template_name="registration/login.html"), name="login"), 
  #  url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    # 위의 문장을 아래처럼 수정하니, 로그아웃 창이 생성됨
    url(r'^accounts/logout/$', views.LogoutView, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('blog.urls')),
]

