from django.shortcuts import render, get_object_or_404, redirect

from app.models.Comercial import Comercial
from app.Forms.ComercialForm import ComercialForm



def comercial_list(request):
    comerciales = Comercial.objects.all()
    return render(request, 'Comercial.html',
                  {'comerciales': comerciales})

def comercial_detail(request, pk):
    comercial = get_object_or_404(Comercial, pk=pk)
    return render(request, 'Comercial.html',
                  {'comercial': comercial})

def comercial_new(request):
    if request.method == "POST":
        form = ComercialForm(request.POST)
        if form.is_valid():
            comercial = form.save()
            return redirect('Comercial.html', pk=comercial.pk)
    else:
        form = ComercialForm()
    return render(request, 'Comercial.html',
                  {'form': form})

def comercial_edit(request, pk):
    comercial = get_object_or_404(Comercial, pk=pk)
    if request.method == "POST":
        form = ComercialForm(request.POST, instance=comercial)
        if form.is_valid():
            comercial = form.save()
            return redirect('comercial_detail', pk=comercial.pk)
    else:
        form = ComercialForm(instance=comercial)
    return render(request, 'Comercial.html',
                  {'form': form})

def comercial_delete(request, pk):
    comercial = get_object_or_404(Comercial, pk=pk)
    if request.method == 'POST':
        comercial.delete()
        return redirect('comerciales')
    return render(request, 'Comercial.html',
                  {'object': comercial})
