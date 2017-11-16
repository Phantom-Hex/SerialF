from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^extra/', include([
		url(r'^$', views.ItemList.as_view(), name='device-list'),
		url(r'^create/$', views.ItemCreation.as_view(), name='device-create'),
		url(r'^(?P<pk>\d+)/', include([
			url(r'^$', views.ItemDetail.as_view(), name='device-detail'),
			url(r'^update/$', views.ItemUpdate.as_view(), name='device-update'),
			url(r'^delete/$', views.ItemDelete.as_view(), name='device-delete'),
		])),
	])),
	url(r'^types/', include([
		url(r'^$', views.TypeList.as_view(), name='type-list'),
		url(r'^create/$', views.TypeCreation.as_view(), name='type-create'),
		url(r'^(?P<pk>\d+)/', include([
			url(r'^$', views.TypeDetail.as_view(), name='type-detail'),
			url(r'^update/$', views.TypeUpdate.as_view(), name='type-update'),
			url(r'^delete/$', views.TypeDelete.as_view(), name='type-delete'),
		])),
	])),
]