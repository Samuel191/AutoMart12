from django.shortcuts import render

# Create your views here. funcion render arma la pagina
def index(request):
    return render(request, "index.html",{"autos":autos})


class Auto:
    def __init__(self, nombre, precio, modelo, color):
        self.nombre = nombre
        self.precio = precio
        self.modelo = modelo
        self.color = color
        

autos =[
    Auto("VW Jetta", 145000, 2018, "Gris"),
    Auto("lexus",256000,2017,"Rojo"),
    Auto("Hot Road", 0, 1954, "custom"),
    Auto("Porsche", 500000, 2017, "rojo")
]
