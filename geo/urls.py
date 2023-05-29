from django.urls import path, include
from rest_framework import routers
from .views import PlaceViewSet, NearestPlaceView

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet, basename='place')

urlpatterns = [
    path('', include(router.urls)),
    path('places/<int:pk>/approve/', PlaceViewSet.as_view({'patch': 'approve_place'}), name='place-approve'),
    path('nearest/', NearestPlaceView.as_view(), name='place-nearest'),
]

app_name = "geo"
