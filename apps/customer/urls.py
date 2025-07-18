from django.urls import path
from . import views


urlpatterns = [
  path('add-new-customer/',views.add_customer, name='add_customer'),
  path('add-template/',views.add, name='add_template'),
  path('search-template/',views.search, name='search_template'),
  path('',views.landing_page, name='landing_page'),
  path('all-customer/',views.customer_list, name ='all_customer'),
  path('login/',views.login_user,name='login'),
  path('signup/',views.signup_user,name='signup'),
  path('logout/',views.user_logout,name='logout'),
  path('customer-edit/<int:id>/',views.customer_edit,name='customer_edit'),
  path('customer-delete/<int:id>/',views.delete_customer,name='delete_customer'),


  
]
