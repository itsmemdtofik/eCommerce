from re import template
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

from app.forms import LoginForm
urlpatterns = [
    
    path('', views.ProductView.as_view(), name = "home"),

    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),

    path('AddToCart/', views.AddToCart, name='AddToCart'),

    path('buy/', views.buy_now, name='buy-now'),

    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('address/', views.address, name='address'),

    path('orders/', views.orders, name='orders'),

    path('mobile/', views.mobile, name='mobile'),
    
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('laptop/', views.laptop, name = 'laptop'),

    path('laptop/<slug:data>', views.laptop, name = 'laptopdata'),

    path('bottomwear/', views.bottomwear, name = 'bottomwear'),

    path('bottomwear/<slug:data>', views.bottomwear, name ='bottomweardata'),

    path('topwear/', views.topwear, name = 'topwear'),

    path('topwear/<slug:data>', views.topwear, name ='topweardata'),

    path('accounts/login', auth_views.LoginView.as_view(template_name = 'app/login.html', authentication_form = LoginForm), name = 'login'),

    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name = 'app/changepassword.html', form_class = MyPasswordChangeForm, success_url = '/passwordchanged/'), name = 'changepassword'),

    path('logout/', auth_views.LogoutView.as_view(next_page = 'login'), name = 'logout'),

    path('passwordchanged/', auth_views.PasswordChangeView.as_view(template_name = 'app/passwordchanged.html'), name = 'passwordchanged'),

    path('resetpassword/', auth_views.PasswordResetView.as_view(template_name = 'app/password_reset.html', form_class = MyPasswordResetForm), name='password_reset'),

    path('resetpassword/successfully/', auth_views.PasswordResetDoneView.as_view(template_name = 'app/password_reset_done.html'), name='password_reset_done'),

    path('resetpassword/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'app/password_reset_confirm.html',form_class = MySetPasswordForm), name='password_reset_confirm'),
    
    path('resetpassword/successfully/completed/', auth_views.PasswordResetCompleteView.as_view(template_name = 'app/password_reset_complete.html'), name='password_reset_complete'),

    path('checkout/', views.checkout, name='checkout'),

    path('registration/', views.CustomerRegistrationView.as_view(),name='customerregistration'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
