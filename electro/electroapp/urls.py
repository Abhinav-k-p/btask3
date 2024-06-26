from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm

urlpatterns = [
    path("", views.home,name="home"),
    path("about/", views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("category-title/<val>", views.CategoryTitle.as_view(), name="category-title"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(), name="product-detail"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("address/", views.address, name="address"),
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"), 
    path("cart/", views.show_cart, name="showcart"),
    path("checkout/", views.show_cart, name="checkout"),
    path('removecart/',views.remove_cart),
    
    
    
    #login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('login/', views.loginuser, name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    #  path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', views.LogoutView, name='logout'),




    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
