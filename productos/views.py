from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Categoria, Producto

# Create your views here.


def index(request):
    # productos = Producto.objects.all()
    # productos = Producto.objects.filter(puntaje=3)
    # # productos = Producto.objects.filter(puntaje__gte=3) # mayor o igual y con lte menor o igual /tambien tenemos gt o lt
    # productos = Producto.objects.get(id=1)
    # productos = Producto.objects.get(pk=1)

    # print(productos)
    # return HttpResponse(productos[0].nombre)

    productos = Producto.objects.all().values()

    # JsonResponse necesita devolver un diccionario
    return JsonResponse(list(productos), safe=False)
