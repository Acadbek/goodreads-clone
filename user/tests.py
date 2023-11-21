from django.test import TestCase
from user.models import CustomUser
from django.contrib.auth import get_user
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def setUp(self):
        self.register_url = reverse('user:register')

    def test_user_account_is_created(self):
        self.client.post(
            self.register_url,
            data={
                "username": 'Anna',
                'first_name': 'Annaliza',
                'last_name': 'Jakonda',
                'email': 'liza@gmail.com',
                'password': 'liza'
            }
        )

        user = CustomUser.objects.get(username='Anna')

        self.assertEqual(user.username, 'Anna')
        self.assertEqual(user.first_name, 'Annaliza')
        self.assertEqual(user.last_name, 'Jakonda')
        self.assertEqual(user.email, 'liza@gmail.com')
        self.assertNotEqual(user.password, 'liza')
        self.assertTrue(user.check_password('liza'))

    def test_required_fields(self):
        response = self.client.post(self.register_url, data={
            'username': '',
            'password': ''
        })

        self.assertEqual(CustomUser.objects.count(), 0)

        expected_errors = {
            'username': ['This field is required.'],
            'password': ['This field is required.'],
            # Add more fields as needed (first_name, last_name, email, etc.)
        }

        for field, errors in expected_errors.items():
            with self.subTest(field=field):
                self.assertFormError(response, 'form', field, errors)

    def test_unique_username(self):
        # 1. create a user
        user = CustomUser.objects.create_user(username='liza', first_name='Monaliza')
        user.set_password('liza')
        user.save()

        # 2. try to create another user with the same username
        response = self.client.post(
            self.register_url,
            data={
                "username": 'liza',
                'first_name': 'Monaliza',
                'last_name': 'Jakonda',
                'email': 'liza@gmail.com',
                'password': 'liza'
            }
        )

        # 3. check that the second user was not created
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 1)

        # 4. check that the form contains the error message
        self.assertFormError(response, 'form', 'username',
                             'A user with that username already exists.')


class LoginTestCase(TestCase):
    def setUp(self):
        self.db_user = CustomUser.objects.create(
            username='assad', first_name='Asadbek')
        self.db_user.set_password('assad')
        self.db_user.save()

    def test_successful_login(self):
        self.client.post(
            reverse('user:login'),
            data={
                'username': 'assad',
                'password': 'assad'
            }
        )

        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)

    def test_logout(self):
        self.client.login(username='assad', password='assad')

        self.client.get(reverse('user:logout'))

        user = get_user(self.client)

        self.assertFalse(user.is_authenticated)


class ProfileTestCase(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse('user:profile'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse(
            'user:login')+'?next=/users/profile/')

    def test_profile_details(self):
        user = CustomUser.objects.create_user(
            username='liza',
            first_name='Monaliza',
            last_name='Djakonda',
            email='mona@gmail.com',
        )
        user.set_password('liza')
        user.save()

        self.client.login(username='liza', password='liza')
        response = self.client.get(reverse('user:profile'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.username)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)


class AdminPageTestCase(TestCase):
    def test_admin_page(self):
        response = self.client.post('/admin/')
        self.assertEqual(response.status_code, 302)


class ProfileUpdateTestCase(TestCase):
    def test_profile_update_form_submission(self):
        user = CustomUser.objects.create(
            username='zemeister',
            first_name='Zemeister',
            last_name='Zem',
            email='zemeister@xmail.zzz'
        )

        user.set_password('zxz')
        user.save()
        self.client.login(username='zemeister', password='zxz')  

        response = self.client.post(
            reverse('user:profile-edit'),
            data={
                'username': 'azzzad',
                'first_name': 'Zemeister',
                'last_name': 'xemex',
                'email': 'xxx@gmail.xxx'
            }
        )

        user = CustomUser.objects.get(pk=user.pk) # OR user.refresh_from_db()

        self.assertEqual(user.username, 'azzzad')
        self.assertEqual(user.first_name, 'Zemeister')
        self.assertEqual(response.url, reverse('user:profile'))
