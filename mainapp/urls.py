from django.urls import path
from . import views
urlpatterns = [
    path('main/', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('swipe/', views.swipe, name='swipe'),
    path('mypage/', views.mypage, name='mypage'),
    path('detail/<int:food_id>', views.detail, name='detail'),
    path('like/', views.like, name='like'),
]