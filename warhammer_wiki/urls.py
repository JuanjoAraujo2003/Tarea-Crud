from django.urls import path, include
from rest_framework import routers
from .views import FactionView, index
from .views import delete_faction, update_faction
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register(r'factions', FactionView, 'factions')
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("", login_required(index), name="index"),
    path("delete/<int:id>/", login_required(delete_faction), name="delete_faction"),
    path("update/<int:id>/", login_required(update_faction), name="update_faction"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
