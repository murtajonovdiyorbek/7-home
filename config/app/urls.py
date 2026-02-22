from django.urls import path
from .views import home, services_detail, services_by_category, mechanic_detail, create_mechanic, create_service, create_category, update_service, update_category, update_mechanic, delete_service, delete_category, delete_mechanic

urlpatterns = [
    path("", home, name="home"),
    path("category/<int:category_id>/", services_by_category, name="services_by_category"),
    path("service/<int:services_id>/", services_detail, name="services_detail"),
    path("mechanic/<int:mechanic_id>/", mechanic_detail, name="mechanic_detail"),
    path("create/", create_mechanic, name="create_mechanic"),
    path("category/", create_category, name="create_category"),
    path("service/", create_service, name="create_service"),

    path("category/<int:pk>/update/", update_category, name="update_category"),
    path("category/<int:pk>/delete/", delete_category, name="delete_category"),
    path("mechanic/<int:pk>/update/", update_mechanic, name="update_mechanic"),
    path("mechanic/<int:pk>/delete/", delete_mechanic, name="delete_mechanic"),
    path("service/<int:pk>/update/", update_service, name="update_service"),
    path("service/<int:pk>/delete/", delete_service, name="delete_service"),
]