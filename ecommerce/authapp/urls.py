from django.urls import path
from . import views
app_name='authapp'
urlpatterns=[
    path('signup/',views.signup),
    path('login/',views.login),
    path('my_logout',views.my_logout),
    path('signup/otpvalidation',views.otpvalidation),
]