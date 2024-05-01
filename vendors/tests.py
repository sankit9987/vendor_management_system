from rest_framework.test import APITestCase


class TestVendor(APITestCase):
    def setUp(self):
        self.data = {
            "name": "test",
            "address": "test",
            "contact_number": 9999999999,
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_create_vendor_without_data(self):
        resp = self.client.post(
            "http://127.0.0.1:8000/api/vendors",
        )
        self.assertEqual(resp.status_code, 400)

    def test_create_vendor_with_data(self):
        resp = self.client.post(
            "http://127.0.0.1:8000/api/vendors",
            self.data,
        )
        self.assertEqual(resp.status_code, 201)

    def test_list_vendors(self):
        resp = self.client.get(
            "http://127.0.0.1:8000/api/vendors",
        )
        self.assertEqual(resp.status_code, 200)

    def test_update_vendor_details(self):
        resp = self.client.patch(
            "http://127.0.0.1:8000/api/vendors/1",
            self.data,
        )
        self.assertEqual(resp.status_code, 200)

    def test_delete_vendor_details(self):
        resp = self.client.patch(
            "http://127.0.0.1:8000/api/vendors/1",
        )
        self.assertEqual(resp.status_code, 204)

    def test_get_vendor_performance(self):
        resp = self.client.get(
            "http://127.0.0.1:8000/api/vendors/1/performace",
        )
        self.assertEqual(resp.status_code, 200)
