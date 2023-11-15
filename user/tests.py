from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(
            reverse('user:register'),
            data={
                "username": 'Anna',
                'first_name': 'Annaliza',
                'last_name': 'Jakonda',
                'email': 'liza@gmail.com',
                'password': 'liza'
            }
        )

        user = User.objects.get(username='Anna')

        self.assertEqual(user.username, 'Anna')
        self.assertEqual(user.first_name, 'Annaliza')
        self.assertEqual(user.last_name, 'Jakonda')
        self.assertEqual(user.email, 'liza@gmail.com')
        self.assertNotEqual(user.password, 'liza')
        self.assertTrue(user.check_password('liza'))

    def test_required_fields(self):
        response = self.client.post(
            reverse('user:register'),
            data={
                'username': 'Anna',
                'password': 'liza'
            }
        )

        user_count = User.objects.count()
        
        self.assertEqual(user_count, 0)
        
        self.assertFormError(response, 'form', 'username',
                             'This field is required.')
        self.assertFormError(response, 'form', 'password',
                             'This field is required.')
