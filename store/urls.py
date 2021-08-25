from django.urls import path
from . import views

urlpatterns = [
path('store/', views.store, name = "store"),
path('cart/', views.cart, name = "cart"),
path('profile/', views.profile, name = "profile"),
path('checkout/', views.checkout, name = "checkout"),
path('shop/', views.shop, name = "shop"),

path('dealer_register/', views.dealer_register, name = "dealer_register"),
path('dealer_info/', views.dealer_info, name = "dealer_info"),
path('dealer_login/', views.dealer_login, name = "dealer_login"),
path('dealer_home/', views.dealer_home, name = "dealer_home"),
path('dealer_product/', views.dealer_product, name = "dealer_product"),
path('dealer_logout/', views.dealer_logoutsite, name = "dealer_logout"),

path('ship_register/', views.ship_register, name = "ship_register"),
path('ship_info/', views.ship_info, name = "ship_info"),
path('ship_login/', views.ship_login, name = "ship_login"),
path('ship_home/', views.ship_home, name = "ship_home"),
path('ship_logout/', views.ship_logoutsite, name = "ship_logout"),
path('out_for/', views.out_for, name = "out_for"),
path('delivery/', views.delivery, name = "delivery"),
path('shipped/', views.shipped, name = "shipped"),
path('ship_home_product/<int:ship_home_product_id>', views.ship_home_product, name="ship_home_product"),
path('shipped_product/<int:shipped_product_id>', views.shipped_product, name="shipped_product"),
path('out_for_product/<int:out_for_product_id>', views.out_for_product, name="out_for_product"),
path('delivery_product/<int:delivery_product_id>', views.delivery_product, name="delivery_product"),

path('register/', views.register, name = "register"),
path('', views.login, name = "login"),
path('logout/', views.logoutsite, name = "logout"),
path('info/', views.info, name = "info"),

path('require/', views.require, name = "require"),
path('search/', views.search, name = "search"),
path('product/<int:product_id>', views.product, name = "product"),
path('category/<int:category_id>', views.category, name = "category"),
path('entity/<int:entity_id>', views.entity, name = "entity"),
path('require_delete/<int:require_id>', views.delete_require, name="require_delete"),
path('order_placed/<int:orderItem_id>', views.order_placed, name="order_placed"),
path('order_detail/<int:orderItem_id>', views.order_detail, name="order_detail"),

path('update_item/', views.updateItem, name = "update_item"),
path('process_order/', views.processOrder, name = "process_order"),
]
