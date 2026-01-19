from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from core.api.views.auth import (
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView,
    MeAPIView,
)

from core.api.views.customer import CustomerViewSet
from core.api.views.task import TaskViewSet
from core.api.views.lead import LeadViewSet
from core.api.views.deal import DealViewSet


router = DefaultRouter()
router.register("customers", CustomerViewSet, basename="customer")
router.register("tasks", TaskViewSet, basename="task")
router.register("leads", LeadViewSet, basename="lead")
router.register("deals", DealViewSet, basename="deal")


urlpatterns = [
    # Auth
    path("auth/register/", RegisterAPIView.as_view()),
    path("auth/login/", LoginAPIView.as_view()),
    path("auth/logout/", LogoutAPIView.as_view()),
    path("auth/me/", MeAPIView.as_view()),
    # JWT refresh
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Router APIs
    path("", include(router.urls)),
]
