from django.urls import path
from. import views
urlpatterns = [
 path('',views.dashboard,name='dashboard'),
 path('profile/<str:pk>/',views.profile,name='profile'),
 path('create_order/',views.create_order_user,name='create_order_user'),
 path('product/',views.product,name='products'),
 path('login_page/',views.login_page,name='login'),
 path('logout_page/',views.logout_page,name='logout_page'),
 path('register/',views.user_register,name='register_page'),
 path('customer/<str:pk>/',views.customer,name='customer'),
 path('create/',views.create_order,name='create_order'),
 path('create_customer/',views.create_customer,name='create_customer'),
 path('create_product/',views.create_product,name='create_product'),
 path('update_customer/<str:pk>/',views.update_customer,name='update_customer'),
 path('delete_customer/<str:pk>/',views.delete_customer,name='delete_customer'),
 path('update/<str:pk>/',views.update_order,name='update_order'),
 path('delete_order/<str:pk>/',views.delete_order,name='delete_order'),
 path('delete_product/<str:pk>/',views.delete_product,name='delete_product'),

]