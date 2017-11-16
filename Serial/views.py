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
	template_name = 'extra/device_list.html'


class ItemDetail(DetailView):
	model = Device
	context_object_name = 'device'
	template_name = 'extra/device_detail.html'


class ItemCreation(CreateView):
	model = Device
	fields = ['name', 'type', 'maker', 'description', 'SKU', 'photo']
	template_name = 'form.html'


class ItemUpdate(UpdateView):
	model = Device
	fields = ['name', 'type', 'maker', 'description', 'SKU', 'photo']
	template_name = 'form.html'


class ItemDelete(DeleteView):
	model = Device
	template_name = 'extra/confirm.html'
	success_url = reverse_lazy('device-list')


# Views for editing types

class TypeList(ListView):
	model = Type
	context_object_name = 'types'
	queryset = Type.objects.all()
	template_name = 'extra/type_list.html'


class TypeDetail(DetailView):
	model = Type
	context_object_name = 'type'
	template_name = 'extra/type_detail.html'


class TypeCreation(CreateView):
	model = Type
	fields = ['type_name', 'type_size']
	template_name = 'form.html'
	success_url = reverse_lazy('type-list')


class TypeUpdate(UpdateView):
	model = Type
	fields = ['type_name', 'type_size']
	template_name = 'form.html'
	success_url = reverse_lazy('type-list')


class TypeDelete(DeleteView):
	model = Type
	template_name = 'extra/confirm.html'
	success_url = reverse_lazy('type-list')