from django.test import TestCase
from customers.models import Customers
from .models import Discount_code, Good
from staff.models import Staff
from django.contrib.auth.models import User


class CustomersDetailTest(TestCase):
    def test_pages_customer(self):
        from django.test import Client
        client = Client()
        user1 = User.objects.create(
            username="test",
            email='test@mail.ru',
            password='12345678',
        )
        customer1 = Customers.objects.create(
            user=user1,
        )
        response = client.get('/customers/1/')
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(Customers.objects.all().count(), 1)
        self.assertEqual(response.status_code, 200)

    def test_pages_customer_staff(self):
        from django.test import Client
        client = Client()
        user1 = User.objects.create(
            username="test",
            email='test@mail.ru',
            password='12345678',
        )
        customer1 = Customers.objects.create(
            user=user1,
        )
        response = client.get('/customers/staff/1/')
        self.assertEqual(response.status_code, 200)

    def test_discount_customer_staff(self):
        from django.test import Client
        client = Client()
        user1 = User.objects.create(
            username="test",
            email='test@mail.ru',
            password='12345678',
        )
        customer1 = Customers.objects.create(
            user=user1,
        )
        user2 = User.objects.create(
            username="test_stuff",
            email='test2@mail.ru',
            password='12345678',
        )
        staff1 = Staff.objects.create(
            user=user2,
        )
        good1 = Good.objects.create(
            name='name',
        )
        code = Discount_code.objects.create(code='1-A-1-A',
                      good=good1,
                      customer=customer1,
                      staff=staff1)
        self.assertEqual(Discount_code.objects.all().count(), 1)
        response = client.get('/customers/staff/1/')
        self.assertContains(response, "1-A-1-A")
        self.assertContains(response, "name")
        self.assertContains(response, "test")
        self.assertContains(response, "test_stuff")

    def test_discount_customer(self):
        from django.test import Client
        client = Client()
        user1 = User.objects.create(
            username="test",
            email='test@mail.ru',
            password='12345678',
        )
        customer1 = Customers.objects.create(
            user=user1,
        )
        user2 = User.objects.create(
            username="test_stuff",
            email='test2@mail.ru',
            password='12345678',
        )
        staff1 = Staff.objects.create(
            user=user2,
        )
        good1 = Good.objects.create(
            name='name',
        )
        code = Discount_code.objects.create(code='1-A-1-A',
                                            good=good1,
                                            customer=customer1,
                                            staff=staff1)
        self.assertEqual(Discount_code.objects.all().count(), 1)
        response = client.get('/customers/staff/1/')
        self.assertContains(response, "1-A-1-A")
        self.assertContains(response, "name")




class Pages_statuscode_Test(TestCase):
    def test_pages_user_search(self):
        from django.test import Client
        client = Client()
        response = client.get('/goods/user_search/')
        self.assertEqual(response.status_code, 200)

    def test_pages_discount(self):
        from django.test import Client
        client = Client()
        user1 = User.objects.create(
            username="test",
            email='test@mail.ru',
            password='12345678',
        )
        customer1 = Customers.objects.create(
            user=user1,
        )
        response = client.get('/goods/discount/1/')
        self.assertEqual(response.status_code, 200)



