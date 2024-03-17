from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView
# from views import RegisterUserView, LoginUserView, LogoutUserView

urlpatterns = [
    path('user/register/', RegisterUserView.as_view(), name = 'register'),
    path('login/', LoginUserView.as_view(), name = 'login'),
    path('user/logout/', LogoutUserView.as_view(), name = 'logout'),
]
