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

    def test_unique_username(self):
        # 1. create a user
        user = User.objects.create_user(username='liza', first_name='Monaliza')
        user.set_password('liza')
        user.save()

        # 2. try to create another user with the same username
        response = self.client.post(
            reverse('user:register'),
            data={
                "username": 'Anna',
                'first_name': 'Annaliza',
                'last_name': 'Jakonda',
                'email': 'liza@gmail.com',
                'password': 'liza'
            }
        )

        # 3. check that the second user was not created
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

        # 4. check that the form contains the error message
        self.assertFormError(response, 'form', 'username',
                             'A user with that username already exists.')
