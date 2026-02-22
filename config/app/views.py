from django.shortcuts import render, redirect
from django.http import HttpRequest

from .models import Service, ServiceCategory, Mechanic
from .forms import MechanicForm, ServiceForm, ServiceCategoryForm

def home(request):
    services_categories = ServiceCategory.objects.all()
    services = Service.objects.all()
    mechanics = Mechanic.objects.all()

    context = {
        "services_categories": services_categories,
        "services": services,
        "mechanics": mechanics
    }

    return render(request, "app/index.html", context)


def services_by_category(request, category_id):
    services_categories = ServiceCategory.objects.all()
    services = Service.objects.filter(category_id=category_id)
    mechanics = Mechanic.objects.all()

    context = {
        "services_categories": services_categories,
        "services": services,
        "mechanics": mechanics
    }

    return render(request, "app/index.html", context)

def mechanic_detail(request, mechanic_id):
    mechanic = Mechanic.objects.get(id=mechanic_id)

    context = {
        "mechanic": mechanic
    }

    return render(request, "app/mechanic.html", context)

def services_detail(request, services_id):
    services = Service.objects.get(id=services_id)

    context = {
        "services": services
    }

    return render(request, "app/services.html", context)


def create_mechanic(request):
    if request.method == "POST":
        form = MechanicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MechanicForm()

    return render(request, "app/create_services.html", {"form": form})


def create_category(request):
    if request.method == "POST":
        form = ServiceCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ServiceCategoryForm()
    return render(request, "app/create_services.html", {"form": form})

def create_service(request):
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ServiceForm()
    return render(request, "app/create_services.html", {"form": form})



def update_category(request: HttpRequest, pk):
    category = ServiceCategory.objects.get(pk=pk)

    if request.method == 'POST':
        form = ServiceCategoryForm(data=request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = ServiceCategoryForm(instance=category)
    context = {"form": form, "category": category}
    return render(request, "app/create_services.html", context)


def delete_category(request: HttpRequest, pk):
    category = ServiceCategory.objects.get(pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('home')

    context = {"category": category}
    return render(request, "app/delete.html", context)


def update_mechanic(request: HttpRequest, pk):
    mechanic = Mechanic.objects.get(pk=pk)

    if request.method == 'POST':
        form = MechanicForm(data=request.POST, files=request.FILES, instance=mechanic)
        if form.is_valid():
            form.save()
            return redirect('mechanic_detail', mechanic_id=mechanic.id)

    form = MechanicForm(instance=mechanic)
    context = {"form": form, "mechanic": mechanic}
    return render(request, "app/create_services.html", context)


def delete_mechanic(request: HttpRequest, pk):
    mechanic = Mechanic.objects.get(pk=pk)

    if request.method == 'POST':
        mechanic.delete()
        return redirect('home')

    context = {"mechanic": mechanic}
    return render(request, "app/delete.html", context)


def update_service(request: HttpRequest, pk):
    service = Service.objects.get(pk=pk)

    if request.method == 'POST':
        form = ServiceForm(data=request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('services_detail', services_id=service.id)

    form = ServiceForm(instance=service)
    context = {"form": form, "service": service}
    return render(request, "app/create_services.html", context)


def delete_service(request: HttpRequest, pk):
    service = Service.objects.get(pk=pk)

    if request.method == 'POST':
        service.delete()
        return redirect('home')

    context = {"service": service}
    return render(request, "app/delete.html", context)