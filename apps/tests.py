from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from decimal import Decimal

class RegionTests(APITestCase):

    def setUp(self):
        self.url = reverse('region-list')  # region-list manzilingiz to'g'ri
        self.data = {'name': 'Tashkent'}

    def test_create_region(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.data['name'])

    def test_read_region(self):
        # Region yaratish
        self.client.post(self.url, self.data, format='json')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Faqat bir region qaytish kerak
        self.assertEqual(response.data[0]['name'], self.data['name'])
    def test_update_region(self):
        response = self.client.post(self.url, self.data, format='json')
        region_id = response.data['id']

        updated_data = {
            'name': 'Samarkand'
        }

        update_url = reverse('region-detail', args=[region_id])  # Detail URL
        response = self.client.put(update_url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_data['name'])

    def test_delete_region(self):
        response = self.client.post(self.url, self.data, format='json')
        region_id = response.data['id']

        delete_url = reverse('region-detail', args=[region_id])  # Detail URL
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 0)



class DiscountTests(APITestCase):
    def setUp(self):
        self.url = reverse('discount-list')  # URL nomi (routerda discount-list)
        self.data = {
            'discount_value': Decimal('10.00'),
            'valid_from': '2024-01-01',
            'valid_to': '2024-12-31',
            'discount_type': 'fixed'
        }

    def test_create_discount(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)  # 'id' maydoni mavjudligi
        self.assertEqual(response.data['discount_value'], str(self.data['discount_value']))

    def test_read_discount(self):
        # Ma'lumot yaratish
        self.client.post(self.url, self.data, format='json')
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 1)  # Yaratilgan discountni tekshirish
        self.assertEqual(response.data[0]['discount_value'], str(self.data['discount_value']))

    def test_update_discount(self):
        # Ma'lumot yaratish
        create_response = self.client.post(self.url, self.data, format='json')
        discount_id = create_response.data['id']

        updated_data = {
            'discount_value': Decimal('15.00'),
            'valid_from': '2024-02-01',
            'valid_to': '2024-12-31',
            'discount_type': 'fixed'
        }

        # Ma'lumotni yangilash
        response = self.client.put(reverse('discount-detail', args=[discount_id]), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['discount_value'], str(updated_data['discount_value']))

    def test_delete_discount(self):
        # Ma'lumot yaratish
        create_response = self.client.post(self.url, self.data, format='json')
        discount_id = create_response.data['id']

        # Ma'lumotni o'chirish
        response = self.client.delete(reverse('discount-detail', args=[discount_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # O'chirilganini tekshirish
        response = self.client.get(reverse('discount-detail', args=[discount_id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)