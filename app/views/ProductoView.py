from django.shortcuts import render, get_object_or_404, redirect

from app.models.Producto import Producto
from app.Forms.ProductoForm import ProductoForm



def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'Producto.html',
                  {'productoes': productos})

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'Producto.html',
                  {'producto': producto})

def producto_new(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            return redirect('Index.html', pk=producto.pk)
    else:
        form = ProductoForm()
    return render(request, 'Producto.html',
                  {'form': form})

def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            return redirect('producto_detail', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'Producto.html',
                  {'form': form})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productoes')
    return render(request, 'Producto.html',
                  {'object': producto})
