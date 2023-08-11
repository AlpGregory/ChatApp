from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', chat_views.chat_page, name='chat_page'),
    path('auth/login/', LoginView.as_view(
        template_name='chat/login_page.html'), name='login_user'),
    path('auth/logout/', LogoutView.as_view, name='logout_user')
]
