from django.urls import path
from . import views

urlpatterns = [
    path('estoque/list',views.estoqueViews.as_view() , name='estoque_list'),  
    path('estoque/create/',views.estoqueCreateView.as_view(),name='estoque_create'),
    path('estoque/<int:pk>/detail/',views.estoqueDetailView.as_view(), name='estoque_detail'),
]