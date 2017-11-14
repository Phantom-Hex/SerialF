from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from Serial.models import Device, Type


def home(request):
	return render(request, 'home.html')


# Views for showing things

class ItemList(ListView):
	model = Device
	context_object_name = 'devices'
	queryset = Device.objects.all()
	template_name = 'devices/device_list.html'


class ItemDetail(DetailView):
	model = Device
	context_object_name = 'device'
	template_name = 'devices/device_detail.html'


class ItemCreation(CreateView):
	model = Device
	fields = ['name', 'type', 'maker', 'description', 'SKU', 'photo']
	template_name = 'device_form.html'


class ItemUpdate(UpdateView):
	model = Device
	fields = ['name', 'type', 'maker', 'description', 'SKU', 'photo']
	template_name = 'device_form.html'


class ItemDelete(DeleteView):
	model = Device
	template_name = 'devices/confirm.html'
	success_url = reverse_lazy('device-list')


# Views for editing types

class TypeCreation(CreateView):
	model = Type
	fields = ['type_name']
	template_name = 'device_form.html'
	success_url = reverse_lazy('device-list')


class TypeUpdate(UpdateView):
	model = Type
	fields = ['type_name']
	template_name = 'device_form.html'
	success_url = reverse_lazy('device-list')


class TypeDelete(DeleteView):
	model = Type
	template_name = 'devices/confirm.html'
	success_url = reverse_lazy('device-list')