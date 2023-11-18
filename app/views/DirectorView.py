from django.shortcuts import render, get_object_or_404, redirect

from app.models.Director import Director
from app.Forms.DirectorForm import DirectorForm



def director_list(request):
    directores = Director.objects.all()
    return render(request, 'Director.html',
                  {'director': directores})

def director_detail(request, pk):
    director = get_object_or_404(Director, pk=pk)
    return render(request, 'Director.html',
                  {'director': director})

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
