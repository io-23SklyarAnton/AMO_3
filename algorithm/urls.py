from django.urls import path
from . import views

app_name = 'algorithm'

urlpatterns = [
    path('graphs/', views.ShowVariantGraphs.as_view(), name='graphs')
]
