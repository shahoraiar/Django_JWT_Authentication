from django.urls import path
from .views import RestrictedView

urlpatterns = [
    path('api/restricted/', RestrictedView.as_view(), name='restricted'),
]