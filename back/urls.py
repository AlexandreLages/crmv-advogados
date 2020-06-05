from django.urls import path
from . import views

urlpatterns = [
	path('', views.advogado_view, name = 'back_advogado'),
	path('login/', views.login_view, name = 'back_login'),
	path('logout/', views.logout_view, name = 'back_logout'),
	path('dash/home/', views.dash_home_view, name = 'back_dash_home'),
	path('dash/redes/', views.dash_redes_view, name = 'back_dash_redes'),
]