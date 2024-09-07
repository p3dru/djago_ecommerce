"""
URL configuration for backend project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import open_api

schema_view = get_schema_view(
    open_api.Info(
        title="E-commerce backend APIs",
        default_version="v1",
        description="This is the doc for the back",
        #terms_of_service="colocar um link dos termos de serviço se tiver"
        contact=open_api.Contact(email="Colocar um e-mail de contato"),
        license=open_api.License(name="BSD Licence"),
    ),
    public=True,
    permission_classes = (permissions.AllowAny, )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),

    #documentation
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
