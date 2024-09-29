from django.urls import path, include
from rest_framework import routers
from .views import FactionView, index
from .views import delete_faction, update_faction


router = routers.DefaultRouter()
router.register(r'factions', FactionView, 'factions')
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("", index , name="index"),
    path("delete/<int:id>/", delete_faction, name="delete_faction"),
    path("update/<int:id>/", update_faction, name="update_faction"),
]
