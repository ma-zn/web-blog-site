from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # لاستخدام LoginView و LogoutView

urlpatterns = [
    # الصفحات الأساسية
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path("about/", views.about, name="about"),
    path('post/new/', views.create_post, name='create_post'),

    # تسجيل الدخول والخروج
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='blog/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='home'),
        name='logout'
    ),

    # تسجيل مستخدم جديد
    path("register/", views.register, name="register"),
]
