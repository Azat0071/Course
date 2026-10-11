from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from .views import CourseListCreatePutPatchDeleteView
router = routers.DefaultRouter()
router.register('course', CourseListCreatePutPatchDeleteView, basename='course')
urlpatterns = [
    path('course/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]