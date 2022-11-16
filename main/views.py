from django.shortcuts import render, redirect

from main.models import Solution, Service
from main.forms import ContactForm


def home(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'home.html', context=context)

    
def solutions(request):
    solutions = Solution.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('solutions')
    context = {'solutions':solutions, 'form':form}
    return render(request, 'solutions.html', context=context)

        
def services(request):
    service = Service.objects.last()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')
    context = {'service':service, 'form':form}
    return render(request, 'services.html', context=context)