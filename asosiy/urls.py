from django.urls import path
from .views import *

urlpatterns = [
    path('clients/', ClientsView.as_view()),
    path('clients-update/', ClientsUPView.as_view()),
    path('products/', ProductView.as_view()),
]
