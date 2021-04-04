from django.shortcuts import render

def index(request):
	"""The homepage for Pizza Online."""
	return render(request, 'pizza_online/index.html')