from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin456321"
        )
        self.client.force_login(self.admin_user)
        self.driver = get_user_model().objects.create_user(
            username="nova",
            password="nova12356",
            license_number="ASD12345"
        )

    def test_driver_license_number_listed(self):
        url = reverse("admin:taxi_driver_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.driver.license_number)

    def test_driver_detail_license_number_listed(self):
        url = reverse("admin:taxi_driver_change", args=[self.driver.id])
        response = self.client.get(url)

        self.assertContains(response, self.driver.license_number)

    def test_driver_add_license_number_listed(self):
        url = reverse("admin:taxi_driver_add")
        response = self.client.get(url)

        self.assertContains(response, "license_number")