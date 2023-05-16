from django.urls import path
from .views import *

app_name = 'cases'

urlpatterns = [
    #URLS FOR HOME PAGE
    path('', HomeView.as_view(), name='home'),
    
    #URLS FOR CLIENTS
    path('clients', ClientListView.as_view(), name='client_list'),
    path('clients/create/', ClientCreateView.as_view(), name='clients_create'),
    path('clients/<int:pk>/update', ClientUpdateView.as_view(), name='clients_update'),
    path('clients/<int:pk>/delete', ClientDeleteView.as_view(), name='clients_delete'),
    
    # URLS FOR LAWYERS 
    path('lawyers', LawyerListView.as_view(), name='lawyer_list'),
    path('lawyers/create/', LawyerCreateview.as_view(), name='lawyers_create'),
    path('lawyers/<int:pk>/update', LawyerUpdateview.as_view(), name='lawyers_update'),
    path('lawyers/<int:pk>/delete', LawyerDeleteView.as_view(), name='lawyers_delete'),
    
    # URLS FOR CASE
    path('cases', CaseListView.as_view(), name='case_list'),
    path('cases/create/', CaseCreateView.as_view(), name='case_create'),
    path('cases/<int:pk>/update', CaseUpdateView.as_view(), name='case_update'),
    path('cases/<int:pk>/delete', CaseDeleteView.as_view(), name='case_delete'),

]   