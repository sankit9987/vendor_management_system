from rest_framework.test import APITestCase


class TestOrder(APITestCase):
    def setUp(self):
        self.data = {
            "vendor": 1,
            "items": "demo",
            "quantity": 2,
            "status": 1,
            "quality_rate": 0,
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_create_Order_without_data(self):
        resp = self.client.post(
            "http://127.0.0.1:8000/api/orders",
        )
        self.assertEqual(resp.status_code, 400)

    def test_create_Order_with_data(self):
        resp = self.client.post(
            "http://127.0.0.1:8000/api/orders",
            self.data,
        )
        self.assertEqual(resp.status_code, 201)

    def test_list_orders(self):
        resp = self.client.get(
            "http://127.0.0.1:8000/api/orders",
        )
        self.assertEqual(resp.status_code, 200)

    def test_update_Order_details(self):
        resp = self.client.patch(
            "http://127.0.0.1:8000/api/orders/1",
            self.data,
        )
        self.assertEqual(resp.status_code, 200)

    def test_delete_Order_details(self):
        resp = self.client.patch(
            "http://127.0.0.1:8000/api/orders/1",
        )
        self.assertEqual(resp.status_code, 204)

    def test_get_Order_acknowledge(self):
        resp = self.client.post(
            "http://127.0.0.1:8000/api/orders/1/acknowledge",
        )
        self.assertEqual(resp.status_code, 200)
