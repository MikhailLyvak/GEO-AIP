from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import fromstr

from geo.models import Place
from geo.serializers import (
    PlaceSerializer,
    PlaceListSerializer
)


class PlaceListPagination(PageNumberPagination):
    page_size = 3
    max_page_size = 3


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    pagination_class = PlaceListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @action(
        detail=True,
        methods=["get"],
        url_path="approve",
        permission_classes=(IsAdminUser,),
    )
    def approve_place(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.aproved:
            return Response(
                {"detail": "Cannot update an already approved place."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        instance.aproved = True
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Place.objects.all()

        name = self.request.query_params.get("name")

        if name:
            queryset = Place.objects.filter(name__icontains=name)

        if self.request.user.is_superuser:
            return queryset

        return queryset.filter(aproved=True)

    def get_serializer_class(self):
        if self.action == "list":
            return PlaceListSerializer

        return PlaceSerializer


class NearestPlaceView(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def get_object(self):
        latitude = self.request.query_params.get("latitude", None)
        longitude = self.request.query_params.get("longitude", None)

        if latitude is not None and longitude is not None:
            pnt = fromstr(f"POINT({latitude} {longitude})", srid=4326)
            return (
                self.get_queryset()
                .annotate(distance=Distance("geom", pnt))
                .order_by("distance")
                .first()
            )
        else:
            return None
