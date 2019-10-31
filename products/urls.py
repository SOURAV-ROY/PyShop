from django.urls import path, include
from . import views
# views.index()
# products
# products/1/details
# products/new

urlpatterns = [
    path('', views.index)
]
