from django.urls import path

from .views import RegisterView, ActiveView, LogoutView, LoginView

app_name = 'users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('active/<str:active_code>/', ActiveView.as_view(), name='active'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login')
]