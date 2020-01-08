from django.shortcuts import render, get_object_or_404

def index(request):
	context = {}
	return render(request, 'index/index.html', context)

def utilities_color(request):
	return render(request, 'index/utilities_color.html')

def utilities_animation(request):
	return render(request, 'index/utilities_animation.html')

def utilities_border(request):
	return render(request, 'index/utilities_border.html')

def utilities_other(request):
	return render(request, 'index/utilities_other.html')

def buttons(request):
	return render(request, 'index/buttons.html')

def cards(request):
	return render(request, 'index/cards.html')

def login(request):
	return render(request, 'index/login.html')

def register(request):
	return render(request, 'index/register.html')

def forgot_password(request):
	return render(request, 'index/forgot_password.html')

def error(request):
	return render(request, 'index/404.html')

def blank(request):
	return render(request, 'index/blank.html')

def charts(request):
	return render(request, 'index/charts.html')

def tables(request):
	return render(request, 'index/tables.html')

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

# new pages for the actual dashboard

def agregar_personal(request):
	return render(request, 'index/agregar_personal.html')

def agregar_obra(request):
	return render(request, 'index/agregar_obra.html')

def prestamos(request):
	return render(request, 'index/prestamos.html')

def agregar_compra(request):
	return render(request, 'index/agregar_compra.html')
