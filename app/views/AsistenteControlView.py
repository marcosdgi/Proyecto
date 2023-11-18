from django.shortcuts import render, get_object_or_404, redirect

from app.models.AsistenteControl import AsistenteControl
from app.Forms.AsistenteControlForm import AsistenteControlForm



def asistente_list(request):
    asistentes = AsistenteControl.objects.all()
    return render(request, 'AsistenteControl.html',
                  {'asistentees': asistentes})

def asistente_detail(request, pk):
    asistente = get_object_or_404(AsistenteControl, pk=pk)
    return render(request, 'AsistenteControl.html',
                  {'asistente': asistente})

def asistente_new(request):
    if request.method == "POST":
        form = AsistenteControlForm(request.POST)
        if form.is_valid():
            asistente = form.save()
            return redirect('AsistenteControl.html', pk=asistente.pk)
    else:
        form = AsistenteControlForm()
    return render(request, 'AsistenteControl.html',
                  {'form': form})

def asistente_edit(request, pk):
    asistente = get_object_or_404(AsistenteControl, pk=pk)
    if request.method == "POST":
        form = AsistenteControlForm(request.POST, instance=asistente)
        if form.is_valid():
            asistente = form.save()
            return redirect('asistente_detail', pk=asistente.pk)
    else:
        form = AsistenteControlForm(instance=asistente)
    return render(request, 'AsistenteControl.html',
                  {'form': form})

def asistente_delete(request, pk):
    asistente = get_object_or_404(AsistenteControl, pk=pk)
    if request.method == 'POST':
        asistente.delete()
        return redirect('asistentees')
    return render(request, 'C:/Users/Developer/Desktop/proyecto/app/templates/AsistenteControl.html',
                  {'object': asistente})
