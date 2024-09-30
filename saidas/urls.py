from django.urls import path
from . import views

urlpatterns = [
    path('saidas/list',views.saidasviews.as_view() , name='saidas_list'),  
    path('saidas/create/',views.saidascreateview.as_view(),name='saidas_create'),
    path('saidas/<int:pk>/detail/',views.saidasdetailview.as_view(), name='saidas_detail'),
]