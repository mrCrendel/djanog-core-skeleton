"""project URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from rest_framework import permissions
# from rest_framework.documentation import include_docs_urls
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="996 API",
#         default_version='v1',
#         description="REST API for mobile apps",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,)
# )
#
# API_TITLE = '996 API DOCS'
# API_DESCRIPTION = 'NO DESCRIPTION'
#
# v1 = ([
#     path('users/', include('apps.users.urls')),
#     path('pages/', include('apps.pages.urls')),
#     path('manufacture/', include('apps.manufacturer.urls')),
#     path('cart/', include('apps.carts.urls')),
#     path('logistic/', include('apps.logistics.urls')),
#     path('about/', include('apps.abouts.urls')),
#     path('orders/', include('apps.orders.urls')),
#     path('notifications/', include('apps.notifications.urls')),
#     path('subscriptions/', include('apps.subscriptions.urls')),
# ], 'v1')


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    # path('api/v1/', include(v1)),
]


# if 'rosetta' in settings.INSTALLED_APPS:
#     urlpatterns += [
#         path('rosetta', include('rosetta.urls'))
#     ]

if settings.DEBUG:
    # urlpatterns += [
    #     path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    #     path('docs-yasg/', schema_view.with_ui('redoc', cache_timeout=0)),
    # ]

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
