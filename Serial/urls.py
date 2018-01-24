from django.conf.urls import include
from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('devices/', include([
		path('', views.ItemList.as_view(), name='device-list'),
		path('create/', views.ItemCreation.as_view(), name='device-create'),
		path('<int:pk>/', include([
			path('', views.ItemDetail.as_view(), name='device-detail'),
			path('update', views.ItemUpdate.as_view(), name='device-update'),
			path('delete', views.ItemDelete.as_view(), name='device-delete'),
		])),
	])),
	path('types/', include([
		path('', views.TypeList.as_view(), name='type-list'),
		path('create/', views.TypeCreation.as_view(), name='type-create'),
		path('<int:pk>/', include([
			path('', views.TypeDetail.as_view(), name='type-detail'),
			path('update/', views.TypeUpdate.as_view(), name='type-update'),
			path('delete/', views.TypeDelete.as_view(), name='type-delete'),
		])),
	])),
]