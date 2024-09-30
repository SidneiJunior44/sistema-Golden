
from django.urls import path
from .views import formulariorateview, AcompanhamentoListView, formListView

urlpatterns = [
    path('formacompanhamento/create/', formulariorateview.as_view(), name='formacompanhamento'),
    path('facomp/', AcompanhamentoListView.as_view(), name='facomp'),
    path('formacompanhamento/detail/', formListView.as_view(), name='formacompanhamento_detail'),
]