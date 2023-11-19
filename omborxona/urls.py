from django.contrib import admin
from django.urls import path, include
from asosiy.views import BolimlarView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BolimlarView.as_view()),
    path('user/', include('accounts.urls')),
    path('asosiy/', include('asosiy.urls')),
    path('stats/', include('stats.urls')),
    # path('client_update/', client_update),
    # path('clients/', clients),
    # path('product_update/', product_update),
    # path('products/', products),
    # path('stats/', stats),
]
