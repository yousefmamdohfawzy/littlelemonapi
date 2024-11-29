from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path('users/<int:id>/groups/', views.user2group, name='user-group-management'), 
    path('groups/manager/users/',views.manager_group,name='manager_group'),
    path('groups/delivery-crew/users/',views.delivery_crew_group,name='delivery-crew_group'),
    path('menu-items/',views.menuItem.as_view(), name='menu-items'),
    path('menu-items/<int:id>/',views.singlemenuItemlistview.as_view(), name='single-menu-items'),
    path('users/carts/menu-item/<int:menu_id>/', views.add_item_to_cart, name='add-item-to-cart'),
    path('users/carts/me/', views.view_cart, name='view-cart'), # if i make users/cart there is a conflict between the Djoser and my custom URL configurations. Specifically, Djoser uses the users path by default in its endpoints
    path('users/carts/me/', views.flush_cart, name='flush-cart'),
    path('orders/',views.orders,name='orders'),
    path('orders/<int:order_id>/', views.manage_order.as_view(),name='manage_order'),
    path('categories/', views.categories, name="categories"),
    
            
]



