from django.urls import path
from .views import *

urlpatterns = [

    path('health_check', HealthView.as_view(), name='health_check'),
    path('fetch_fact', FetchFact.as_view(), name='fetch_fact'),
    path('get_fact', GetFact.as_view(), name='get_fact'),
]
