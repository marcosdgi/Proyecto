from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from app.models.Producto import Producto
from app.Forms.ProductoForm import ProductoForm





def buscar_producto(request):
    query = request.GET.get('q', '')
    campo = request.GET.get('campo', '')

    if query:  # Solo filtrar si se proporciona un término de búsqueda
        if campo:
            kwargs = {f'{campo}__icontains': query}
            resultados = Producto.objects.filter(**kwargs)
        else:
            q_objects = Q()
            for field in Producto._meta.fields:
                q_objects |= Q(**{f'{field.name}__icontains': query})
            resultados = Producto.objects.filter(q_objects)
    else:
        resultados = Producto.objects.all()  # Devolver todos los objetos si no se proporciona un término de búsqueda

    campos = [field.name for field in Producto._meta.fields]
    return render(request, 'Producto.html', {'resultados': resultados, 'campos': campos})

