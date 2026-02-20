from django.shortcuts import render, redirect

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