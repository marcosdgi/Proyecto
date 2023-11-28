from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from app.models.Director import Director
from app.Forms.DirectorForm import DirectorForm



def director_list(request):
    directores = Director.objects.all()
    return render(request, 'Director.html',
                  {'director': directores})

@login_required()
def buscar_director(request):
    query = request.GET.get('q', '')
    campo = request.GET.get('campo', '')

    if query:  # Solo filtrar si se proporciona un término de búsqueda
        if campo:
            kwargs = {f'{campo}__icontains': query}
            resultados = Director.objects.filter(**kwargs)
        else:
            q_objects = Q()
            for field in Director._meta.fields:
                q_objects |= Q(**{f'{field.name}__icontains': query})
            resultados = Director.objects.filter(q_objects)
    else:
        resultados = Director.objects.all()  # Devolver todos los objetos si no se proporciona un término de búsqueda

    campos = [field.name for field in Director._meta.fields]
    return render(request, 'Director.html', {'resultados': resultados, 'campos': campos})

def director_new(request):
    if request.method == "POST":
        form = DirectorForm(request.POST)
        if form.is_valid():
            director = form.save()
            return redirect('Director.html', pk=director.pk)
    else:
        form = DirectorForm()
    return render(request, 'Director.html',
                  {'form': form})

def director_edit(request, pk):
    director = get_object_or_404(Director, pk=pk)
    if request.method == "POST":
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            director = form.save()
            return redirect('director_detail', pk=director.pk)
    else:
        form = DirectorForm(instance=director)
    return render(request, 'Director.html',
                  {'form': form})

def director_delete(request, pk):
    director = get_object_or_404(Director, pk=pk)
    if request.method == 'POST':
        director.delete()
        return redirect('director')
    return render(request, 'Director.html',
                  {'object': director})
