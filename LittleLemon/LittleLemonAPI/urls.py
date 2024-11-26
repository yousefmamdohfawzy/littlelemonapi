from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path('users/<int:id>/groups/', views.user2group, name='user-group-management'), 
    path('groups/manager/users/',views.manager_group,name='manager_group'),
    path('groups/delivery-crew/users/',views.delivery_crew_group,name='delivery-crew_group'),
    path('menu-items/',views.menuItem.as_view(), name='menu-items'),
    path('menu-items/<int:id>/',views.singlemenuItemlistview.as_view(), name='single-menu-items'),
    path('users/<int:id>/cart/menu-item/<int:menu_id>/', views.add_item_to_cart, name='add-item-to-cart'),
    path('users/<int:id>/cart/menu-item/', views.view_cart, name='view-cart'),
    path('users/<int:id>/cart/', views.flush_cart, name='flush-cart'),
    path('orders/',views.orders,name='orders'),
    path('orders/<int:order_id>/', views.manage_order.as_view(),name='manage_order'),

        
]


