from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('buy/', views.buy, name='buy'),
  path('charge-status/<id>/', views.charge_status, name='status'),
  path('blog/', views.blog, name='blog')
]