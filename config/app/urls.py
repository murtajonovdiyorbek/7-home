from django.urls import path
from .views import home, services_detail, services_by_category, mechanic_detail, create_mechanic, create_service, create_category

urlpatterns = [
    path("", home, name="home"),
    path("category/<int:category_id>/", services_by_category, name="services_by_category"),
    path("service/<int:services_id>/", services_detail, name="services_detail"),
    path("mechanic/<int:mechanic_id>/", mechanic_detail, name="mechanic_detail"),
    path("create/", create_mechanic, name="create_mechanic"),
    path("category/", create_category, name="create_category"),
    path("service/", create_service, name="create_service"),
]