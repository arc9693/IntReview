from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('ListResponses', views.ListResponses, name='ListResponses'),

    path('ListResponses/search', views.ListResponsesbyCompany, name='ListResponsesbyCompany'),

    path('ListResponses/response/<int:response_id>', views.viewResponse, name='viewResponse'),

    path('ListResponses/response/<int:response_id>/update',views.updateResponse, name='updateResponse'),

    path('ListResponses/response/<int:response_id>/delete',views.deleteResponse, name='deleteResponse'),

    path('response/new', views.response_new, name='response_new'),

    path('response/new/addCompany', views.add_company, name='add_company'),

    path('signup', views.signup, name='signup'),

    path('login',views.login_view, name='login'),

    path('logout',views.logout_view, name='logout'),
]
