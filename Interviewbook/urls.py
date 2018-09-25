from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('ListResponses', views.ListResponses, name='ListResponses'),

    path('response/<int:response_id>', views.viewResponse, name='viewResponse'),

    path('response/new', views.response_new, name='response_new'),

    path('response/new/addCompany', views.add_company, name='add_company'),
]
