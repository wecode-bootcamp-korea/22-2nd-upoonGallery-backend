import jwt, json

from django.test import TestCase, Client, RequestFactory

from arts.models  import Art, Artist, Size, Shape
from users.models import User
from carts.models import Cart

from my_settings import SECRET_KEY, ALGORITHM

class CartTest(TestCase):
    def setUp(self):
        User.objects.create(
            id        = 1,
            kakao_id  = "1111",
            email     = "cola@cola.com",
            nick_name = "colada",
            birthday  = "0425",
            gender    = "male"
        )

        User.objects.create(
            id        = 10,
            kakao_id  = "1010",
            email     = "lala@lalala.com",
            nick_name = "lala",
            birthday  = "0101",
            gender    = "male"
        )
        
        Artist.objects.create(id=1, name="YERANG")
        Artist.objects.create(id=2, name="JORDAN")
        
        Size.objects.create(id=1, name=5)
        Size.objects.create(id=2, name=10)

        Shape.objects.create(id=1, name="SEMO")
        Shape.objects.create(id=2, name="NEMO")

        Art.objects.create(
            id          = 1,
            title       = "ART-1",
            image_url   = "ART-1-IMAGE",
            description = "THIS IS ART NO.1",
            price       = 300000,
            artist_id   = 1,
            size_id     = 1,
            shape_id    = 1
        )
        Art.objects.create(
            id          = 2,
            title       = "ART-2",
            image_url   = "ART-2-IMAGE",
            description = "THIS IS ART NO.2",
            price       = 200000,
            artist_id   = 2,
            size_id     = 2,
            shape_id    = 2
        )

        Art.objects.create(
            id          = 3,
            title       = "ART-3",
            image_url   = "ART-3-IMAGE",
            description = "THIS IS ART NO.3",
            price       = 100000,
            artist_id   = 2,
            size_id     = 2,
            shape_id    = 2
        )

        Cart.objects.create(user_id=1, art_id=1)
        Cart.objects.create(user_id=1, art_id=2)
        
    def tearDown(self):
        Art.objects.all().delete()
        Artist.objects.all().delete()
        Size.objects.all().delete()
        Shape.objects.all().delete()
        Cart.objects.all().delete()
        User.objects.all().delete()

    def test_cartview_get_success(self):
        client = Client()

        access_token = jwt.encode({'user_id': 1}, SECRET_KEY, algorithm=ALGORITHM)
        headers      = {'HTTP_Authorization': access_token}

        response = client.get('/carts', **headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                        {
                            'results': [
                                {
                                    "art_id": 1,
                                    "art_title": "ART-1",
                                    "art_price": 300000,
                                    "artist": "YERANG",
                                    "size": 5
                                },
                                {
                                    "art_id": 2,
                                    "art_title": "ART-2",
                                    "art_price": 200000,
                                    "artist": "JORDAN",
                                    "size": 10
                                }

                            ],
                            'total_price': 500000,
                            'count': 2
                        }
        )

    def test_cartview_get_user_does_not_exists(self):
        client = Client()

        access_token = jwt.encode({'user_id': 2}, SECRET_KEY, algorithm=ALGORITHM)
        headers      = {'HTTP_Authorization': access_token}

        response = client.get('/carts', **headers)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message': 'USER_DOES_NOT_EXISTS'})

    def test_cartview_post_success(self):
        client = Client()

        access_token = jwt.encode({'user_id': 1}, SECRET_KEY, algorithm=ALGORITHM)
        
        data    = {'art_id': 3}
        headers = {'HTTP_Authorization': access_token}

        response = client.post(path='/carts', data=data, content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)

    def test_cartview_post_bad_request(self):
        client = Client()

        access_token = jwt.encode({'user_id': 1}, SECRET_KEY, algorithm=ALGORITHM)
        
        data    = {'art_id': 1}
        headers = {'HTTP_Authorization': access_token}

        response = client.post(path='/carts', data=data, content_type='application/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message': 'BAD_REQUEST'})

    def test_cartview_post_art_does_not_exists(self):
        client = Client()

        access_token = jwt.encode({'user_id': 1}, SECRET_KEY, algorithm=ALGORITHM)
        
        data     = {'art_id': 777}
        headers  = {'HTTP_Authorization': access_token}
        
        response = client.post('/carts', data=data, content_type='application/json', **headers)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message': 'ART_DOES_NOT_EXISTS'})

    def test_cartview_delete_success(self):
        client = Client()

        access_token = jwt.encode({'user_id': 1}, SECRET_KEY, algorithm=ALGORITHM)
        headers      = {'HTTP_Authorization': access_token}

        response = client.delete('/carts?art-id=2', **headers)

        self.assertEqual(response.status_code, 200)

    def test_cartview_delete_not_found(self):
        client = Client()

        access_token = jwt.encode({'user_id': 1}, SECRET_KEY, algorithm=ALGORITHM)
        headers      = {'HTTP_Authorization': access_token}

        response = client.delete('/carts?art-id=777', **headers)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'message': 'NOT_FOUND'})
