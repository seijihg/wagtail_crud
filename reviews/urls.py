from django.urls import path, include
from .views import ReviewViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"reviews", ReviewViewSet)

app_name = "reviews"

urlpatterns = [
    path("", include(router.urls)),
]
