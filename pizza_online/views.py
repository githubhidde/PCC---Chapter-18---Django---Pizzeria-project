from django.shortcuts import render

from .models import Pizza

def index(request):
	"""The homepage for Pizza Online."""
	return render(request, 'pizza_online/index.html')

def pizzas(request):
	pizzas = Pizza.objects.order_by('date_added')
	context = {'pizzas': pizzas}
	return render(request, 'pizza_online/pizzas.html', context)