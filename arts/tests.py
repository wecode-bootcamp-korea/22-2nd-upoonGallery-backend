from django.test    import TestCase
from django.test    import Client

from arts.models    import Art, Artist, Size, Shape, Color, ArtColor, Theme, ArtTheme
from carts.models   import Cart 
from reviews.models import ReviewImage, Review
from users.models   import User

class ArtsTest(TestCase):
    def setUp(self):
        User.objects.create(
            id = 1,
            email = "a@gmail.com",
            password = 1234,
            nick_name = "졸려",
            birthday = "2000-01-01",
            gender = "male",
            kakao_id = "1111"
        )

        Artist.objects.create(
            id = 1,
            name = "최현정"
        )

        Size.objects.create(
            id = 1,
            name = 1
        )
        
        Size.objects.create(
            id = 2,
            name = 2,
        )

        Shape.objects.create(
            id = 1,
            name = "가로형"
        )

        Shape.objects.create(
            id = 2,
            name = "세로형"
        )

        Art.objects.create(
            id = 1,
            title = "하루종일 잠만 자고 싶어",
            image_url = "https://pbs.twimg.com/profile_images/1383818413982715911/SewPb-Gm_400x400.jpg",
            description = "에어컨 틀고 이불안에서 12시간 자고 싶어",
            price = "150000.00",
            artist_id = 1,
            size_id = 1,
            shape_id= 1,
        )


        Art.objects.create(
            id = 2,
            title = "오늘은 짜빠게티 요리사",
            image_url = "https://t1.daumcdn.net/liveboard/realfood/ad5e6801850747b29c781aa9e4d57201.JPG",
            description = "룰루",
            price = "150000.00",
            artist_id = 1,
            size_id = 1,
            shape_id= 2,
        )

        Color.objects.create(
            id = 1,
            name = "그린"
        )
        Color.objects.create(
            id = 2,
            name = "레드"
        )

        Theme.objects.create(
            id = 1,
            name = "풍경"
        )

        ArtColor.objects.create(
            # id = id,
            art_id = 1,
            color_id = 1
        )
        ArtColor.objects.create(
            # id = id,
            art_id = 2,
            color_id = 2
        )
        
        ArtTheme.objects.update_or_create(
            id = 1,
            art_id = 1,
            theme_id = 1
        )

        Cart.objects.update_or_create(
            id = 1,
            user_id = 1,
            art_id = 1
        )

        Review.objects.update_or_create(
            id = 1,
            art_id = 1,
            comment = "공감합니다~",
            user_id = 1
        )
        ReviewImage.objects.update_or_create(
            id = 1,
            image_url = "https://storage.googleapis.com/jjalbot-jjals/2018/12/aziS307P5/zzal.jpg", 
            review_id = 1
        )


    def tearDown(self):
        ReviewImage.objects.all().delete()
        Review.objects.all().delete()
        Cart.objects.all().delete()
        ArtTheme.objects.all().delete()
        ArtColor.objects.all().delete()
        Theme.objects.all().delete()
        Color.objects.all().delete()
        Art.objects.all().delete()
        Shape.objects.all().delete()
        Size.objects.all().delete()
        Artist.objects.all().delete()
        User.objects.all().delete()


    def test_art_get_view(self):
        client = Client()
        response = client.get('/arts')

        self.assertEqual(response.status_code,200)
        
        self.assertEqual(response.json(),
        {
        'results': 
                [
                    {
                        'art_id': 1, 
                        'title': '하루종일 잠만 자고 싶어', 
                        'image_url': 'https://pbs.twimg.com/profile_images/1383818413982715911/SewPb-Gm_400x400.jpg', 'artist_name': '최현정',
                        'artist_id': 1, 
                        'size': 1, 
                        'is_available': True, 
                        'price': '150000.00', 
                        'description': '에어컨 틀고 이불안에서 12시간 자고 싶어', 
                        'shape': '가로형'
                    }, 
                    {
                        'art_id': 2,
                        'title': '오늘은 짜빠게티 요리사', 
                        'image_url': 'https://t1.daumcdn.net/liveboard/realfood/ad5e6801850747b29c781aa9e4d57201.JPG', 
                        'artist_name': '최현정', 
                        'artist_id': 1, 
                        'size': 1, 
                        'is_available': True, 
                        'price': '150000.00', 
                        'description': '룰루', 
                        'shape': '세로형'
                    }
                ], 
                'total_count': 2
            })

    def test_art_filter_once_get_view(self):
        client = Client()
        response = client.get('/arts?color=레드')

        self.assertEqual(response.status_code,200)
    
        self.assertEqual(response.json(),
        {
        'results': 
                [
                    {
                    'art_id': 2,
                    'title': '오늘은 짜빠게티 요리사', 
                    'image_url': 'https://t1.daumcdn.net/liveboard/realfood/ad5e6801850747b29c781aa9e4d57201.JPG', 
                    'artist_name': '최현정', 
                    'artist_id': 1, 
                    'size': 1, 
                    'is_available': True, 
                    'price': '150000.00', 
                    'description': '룰루', 
                    'shape': '세로형'
                    }
                ], 
                'total_count': 1
            })

    def test_art_filter_twice_get_view(self):
        client = Client()
        response = client.get('/arts?color=그린&min_price=0&max_price=150000')

        self.assertEqual(response.status_code,200)
        
        self.assertEqual(response.json(),
        {
        'results': 
                [
                    {
                    'art_id': 1, 
                    'title': '하루종일 잠만 자고 싶어', 
                    'image_url': 'https://pbs.twimg.com/profile_images/1383818413982715911/SewPb-Gm_400x400.jpg', 
                    'artist_name': '최현정', 
                    'artist_id': 1, 
                    'size': 1, 
                    'is_available': True, 
                    'price': '150000.00', 
                    'description': '에어컨 틀고 이불안에서 12시간 자고 싶어', 
                    'shape': '가로형'
                    }
                ], 
                'total_count': 1
            })

    def test_art_filter_get_view_fail(self):
        client = Client()
        response = client.get('/arts?limit=[실패]')

        self.assertEqual(response.status_code,400)
        
        self.assertEqual(response.json(),
        {
            "message": "VALUE_ERROR"
        })

class ArtTest(TestCase):
    def setUp(self):
        User.objects.create(
            id = 1,
            email = "jm@gmail.com",
            password = 1234,
            nick_name = "서정민",
            birthday = "2000-01-12",
            gender = "female",
            kakao_id = "1112"
        )

        Artist.objects.create(
            id = 1,
            name = "서정민"
        )

        Size.objects.create(
            id = 1,
            name = 1
        )
        
        Size.objects.create(
            id = 2,
            name = 2,
        )

        Shape.objects.create(
            id = 1,
            name = "세로형"
        )

        Art.objects.create(
            id = 1,
            title = "주지훈",
            image_url = "https://topclass.chosun.com/news_img/2004/2004_056.jpg",
            description = "주지훈보다는 아이유지 by 재현",
            price = "300000.00",
            artist_id = 1,
            size_id = 1,
            shape_id= 1,
        )
        
        Color.objects.create(
            id = 1,
            name = "레드"
        )

        Theme.objects.create(
            id = 1,
            name = "인물"
        )

        ArtColor.objects.create(
            # id = id,
            art_id = 1,
            color_id = 1
        )
        
        ArtTheme.objects.update_or_create(
            id = 1,
            art_id = 1,
            theme_id = 1
        )

    def tearDown(self):
        ArtTheme.objects.all().delete()
        ArtColor.objects.all().delete()
        Theme.objects.all().delete()
        Color.objects.all().delete()
        Art.objects.all().delete()
        Shape.objects.all().delete()
        Size.objects.all().delete()
        Artist.objects.all().delete()
        User.objects.all().delete()

    def test_art_get_view(self):
        client = Client()
        response = client.get('/arts/1')

        self.assertEqual(response.status_code,200)
        
        self.assertEqual(response.json(),
        {
        'art_information': 
                {
                    'id': 1, 
                    'title': '주지훈', 
                    'price': '300000.00', 
                    'size': 1, 
                    'artist_name': '서정민', 
                    'description': '주지훈보다는 아이유지 by 재현', 
                    'image_urls': ['https://topclass.chosun.com/news_img/2004/2004_056.jpg']
                }
            }
        )
    
    def test_art_get_view_fail(self):
        client = Client()
        response = client.get('/arts/100')
        
        self.assertEqual(response.status_code, 404)

        self.assertEqual(response.json(),
        {
            "message": "ART_NOT_FOUND"
        })
