from django.urls import path
from . import views
urlpatterns = [
	path('', views.index, name='index'),
	path('index', views.index, name='index'),
	path('utilities_color', views.utilities_color, name='utilities_color'),
	path('utilities_animation', views.utilities_animation, name='utilities_animation'),
	path('utilities_border', views.utilities_border, name='utilities_border'),
	path('utilities_other', views.utilities_other, name='utilities_other'),
	path('buttons', views.buttons, name='buttons'),
	path('cards', views.cards, name='cards'),
	path('login', views.login, name='login'),
	path('register', views.register, name='register'),
	path('forgot_password', views.forgot_password, name='forgot_password'),
	path('error', views.error, name='error'),
	path('blank', views.blank, name='blank'),
	path('charts', views.charts, name='charts'),
	path('tables', views.tables, name='tables'),
	#new links to the actual dashboard
	path('agregar_personal', views.agregar_personal, name='agregar_personal'),
	path('agregar_obra', views.agregar_obra, name='agregar_obra'),
	path('prestamos', views.prestamos, name='prestamos'),
	path('agregar_compra', views.agregar_compra, name='agregar_compra'),
]
