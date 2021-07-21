import jwt

from django.test   import TestCase, Client
from unittest.mock import patch, MagicMock

from users.models import User
from my_settings  import SECRET_KEY, ALGORITHM

class UserTest(TestCase):
    def setup(self):
        User.objects.create(
            id        = 1,
            kakao_id  = "1816852310",
            email     = "yrchic@hotmail.com",
            nick_name = "yr K",
            birthday  = "0425",
            gender    = "male"
        )

    def tearDown(self):
        User.objects.all().delete()

    @patch('users.views.requests')
    def test_kakao_signin_new_user_success(self, mocked_requests):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
                    "id": "123456789",
                    "kakao_account": { 
                        "email": "blahblah@blah.com",
                        "birthday": "0425",
                        "gender": "male",
                    },
                    "properties": {
                        "nickname": "blahblahblah"
                    }
                }

        mocked_requests.post = MagicMock(return_value = MockedResponse())
        headers              = {"Authorization": "test_token"}
        response             = client.get('/users/signin/kakao', headers=headers)

        access_token = response.json().get('access_token')
        pay_load     = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        user         = User.objects.get(id=pay_load['user_id'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(user.kakao_id, "123456789")

    @patch('users.views.requests')
    def test_kakao_signin_exist_user_success(self, mocked_requests):
        client = Client()

        class MockedResponse:
            def json(self):
                return {
                    "id": "1816852310",
                    "kakao_account": { 
                        "email": "yrchic@hotmail.com",
                        "birthday": "0425",
                        "gender": "male",
                    },
                    "properties": {
                        "nickname": "yr K"
                    }
                }

        mocked_requests.post = MagicMock(return_value = MockedResponse())
        headers              = {"Authorization": "test_token"}
        response             = client.get('/users/signin/kakao', headers=headers)

        access_token = jwt.encode({'user_id': 1}, SECRET_KEY, algorithm=ALGORITHM)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('access_token'), access_token)