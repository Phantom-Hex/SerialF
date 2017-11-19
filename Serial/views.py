from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from Serial.models import Device, Type


def home(request):
	return render(request, 'home.html')


class LoginView(generic.FormView):
	form_class = AuthenticationForm
	success_url = reverse_lazy('home')
	template_name = "form.html"

	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		return form_class(self.request, **self.get_form_kwargs())

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super().form_valid(form)


class LogoutView(generic.RedirectView):
	url = reverse_lazy("home")

	def get(self, request, *args, **kwargs):
		logout(request)
		return super().get(request, *args, **kwargs)


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