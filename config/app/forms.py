from django import forms
from .models import ServiceCategory, Mechanic, Service

class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = "__all__"

class MechanicForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = "__all__"

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"