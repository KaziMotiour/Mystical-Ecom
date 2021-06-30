
from django.urls import path, include
from .views import CreateNewUserView, ChangePasswordView

urlpatterns = [
   
    path('singup/', CreateNewUserView.as_view(), name='singup'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

]
