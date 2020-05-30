from django.urls import path
from . import views

urlpatterns = [
	path('', views.advogado_view, name = 'back_advogado'),
	path('login/', views.login_view, name = 'back_login'),
	path('logout/', views.logout_view, name = 'back_logout'),
]