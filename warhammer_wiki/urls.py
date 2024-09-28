from django.urls import path, include
from rest_framework import routers
from .views import FactionView, index


router = routers.DefaultRouter()
router.register(r'factions', FactionView, 'factions')
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("", index , name="index")
]
