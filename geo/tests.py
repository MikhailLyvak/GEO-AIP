from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.contrib.gis.geos import Point
from rest_framework import status

from geo.models import Place
from user.models import User
from geo.serializers import (
    PlaceSerializer,
    PlaceListSerializer,
)
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

PLACE_URL = reverse("geo:place-list")


class PlaceModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@mail.com", password="testpassword"
        )
        self.place = Place.objects.create(
            user=self.user,
            name="Test Place",
            description="Test description",
            geom=Point(10.0, 20.0, srid=4326),
        )

    def test_place_str_method(self):
        self.assertEqual(str(self.place), "Test Place")


class PointFieldSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@mail.com", password="testpassword"
        )

    def test_to_representation(self):
        serializer = PlaceSerializer()
        point = Point(1.23, 4.56, srid=4326)
        representation = serializer.fields["geom"].to_representation(point)
        expected_representation = {"type": "Point", "coordinates": [1.23, 4.56]}
        self.assertEqual(representation, expected_representation)

    def test_get_geom(self):
        serializer = PlaceListSerializer()
        place_instance = Place.objects.create(
            user=self.user,
            name="Test Place",
            description="Test description",
            geom=Point(1.23, 4.56, srid=4326),
        )
        geom = serializer.fields["geom"].to_representation(place_instance.geom)
        expected_geom = {"type": "Point", "coordinates": [1.23, 4.56]}
        self.assertEqual(geom, expected_geom)


class AuthenticatedPlaceApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "t1e2s3t4",
        )
        self.client.force_authenticate(self.user)

    def test_create_place(self):
        payload = {
            "name": "Test",
            "description": "Test description",
            "geom": "POINT (1 1)",
        }

        res = self.client.post(PLACE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        place = Place.objects.get(id=res.data["id"])
        for key in payload.keys():
            if key == "geom":
                expected = payload[key]
                actual = str(getattr(place, key)).split(";")[1].strip()
                self.assertEqual(expected, actual)
            else:
                self.assertEqual(payload[key], getattr(place, key))
