from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta
from api.forms import Ventaform

# Create your views here.
def index(request):
    return render(request,'index.html')

def catalogo(request):
    return render(request,'catalogo.html')

def formulario(request):
    data = {
    'forms':Ventaform()
    }
    if (request.method == 'POST'):
        formulario = Ventaform(request.POST)
        if(formulario.is_valid()):
            formulario.save()
            data['mensaje'] = "Guardado correctamente "
        else:
            data['mensaje'] = "Error "
    return render(request,"formulario.html", data)

def crud (request):
    venta = Venta.objects.all()
    data = {
    'formu' :venta
    }
    return render(request,'crud.html',data)

def modificar (request, id ):
    producto = get_object_or_404(Venta, id =id)
    data={
    'forms': Ventaform(instance=producto)
    }
    if (request.method == 'POST'):
        formulario = Ventaform(data=request.POST, instance=producto)
        if(formulario.is_valid()):
            formulario.save()
            data['mensaje'] = "Modificado correctamente "
        else:
            data['mensaje'] = "Error "
    return render(request,'modificar.html',data)

def eliminar (request, id ):
    venta = get_object_or_404(Venta, id = id)
    venta.delete()
    return redirect(to="/crud") 
