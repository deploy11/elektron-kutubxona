from django.urls import path
from .views import home,EditView
from .user_views import *

urlpatterns = [
    path('',home,name='home'),
    path('e/<int:pk>',EditView.as_view(),name='edit'),
    # user urls
    path('login/???/',LoginPage,name='login'),
    path('logout/???/',LogoutPage,name='logout'),
]
