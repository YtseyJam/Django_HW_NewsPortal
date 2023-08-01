from django.urls import path
from .views import SignUp

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    # path('upgrade', upgrade_user, name='account_upgrade'),
]