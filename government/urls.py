from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('governmentdata', views.GovernmentDataView)


urlpatterns = [
    path('', include(router.urls)),
]