from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth import views as auth_views
from racks import views

urlpatterns = [
    path('', views.index, name="home"),
    path('book/list/', views.BookListView.as_view(), name="book-list"),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.logout, {'next_page': 'login'}, name='logout'),
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('list/', views.RackListView.as_view(), name="rack-list"),
    path('<int:pk>/detail/', views.RackDetailView.as_view(), name="rack-detail" )
]