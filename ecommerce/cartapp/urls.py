from django.urls import path
from . import views
from django.conf.urls import include

app_name='cartapp'
urlpatterns=[
    path('addcart',views.addcart,name='addcart'),
    path('insertcart',views.insertcart,name='insertcart'),
    path('cart/',views.cart,name='cart'),
    path('deletecart',views.deletecart,name='delete'),
    path('modifycart',views.modifycart,name='modifycart'),
    path('modifiedcart/',views.modifiedcart,name='modifiedcart'),
    path('views',views.viewcart),
]