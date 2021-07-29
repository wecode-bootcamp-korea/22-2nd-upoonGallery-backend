from django.test    import TestCase, Client

from users.models   import User
from arts.models    import Art, Artist, Size, Shape
from reviews.models import Review, ReviewImage

class ReviewTest(TestCase):
    def setUp(self):
        User.objects.create(
            id        = 1,
            email     = "chim@gmail.com",
            password  = "1234",
            nick_name = "침착맨",
            birthday  = "2021-07-28",
            gender    = "male",
            kakao_id  = "210728"
        )
        
        User.objects.create(
            id        = 2,
            email     = "pearl@gmail.com",
            password  = "1234",
            nick_name = "주펄",
            birthday  = "2021-07-28",
            gender    = "male",
            kakao_id  = "210729"
        )
        
        Artist.objects.create(
            id   = 1,
            name = "침착맨"
        )

        Size.objects.create(
            id   = 10,
            name = 10
        )

        Shape.objects.create(
            id   = 2,
            name = "세로형"
        )

        Art.objects.create(
            id           = 1,
            title        = "오히려좋아",
            image_url    = "https://upoonbucket.s3.us-east-2.amazonaws.com/evenbetter",
            description  = "와장창",
            price        = 20000,
            artist_id    = 1,
            size_id      = 10,
            shape_id     = 2,
            is_available = True
        )
     
        Review.objects.create(
            id      = 1,
            user_id = 1,
            art_id  = 1,
            comment = "와장창와장창"
        )
        
        Review.objects.create(
            id      = 2,
            user_id = 2,
            art_id  = 1,
            comment = "평화주의작"
        )
        
        ReviewImage.objects.create(
            id        = 1,
            review_id = 1,
            image_url = "https://upoonbucket.s3.us-east-2.amazonaws.com/wajangchnag"    
        )
        
        ReviewImage.objects.create(
            id        = 2,
            review_id = 2,
            image_url = "https://upoonbucket.s3.us-east-2.amazonaws.com/innerpeace" 
        )
        
    def tearDown(self):
        ReviewImage.objects.all().delete(),
        Review.objects.all().delete(),
        Artist.objects.all().delete(),
        Size.objects.all().delete(),
        Shape.objects.all().delete(),
        Art.objects.all().delete(),
        User.objects.all().delete()
    
    def test_reviewview_get_success(self):
        client = Client()

        response = client.get('/arts/1/reviews')
        print(response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
            {'message': 'SUCCESS', 'review_data': [
                {
                    'user_id': 1, 
                    'user_nickname': '침착맨', 
                    'art_id': 1, 'comment': '와장창와장창', 
                    'review_image_url': 'https://upoonbucket.s3.us-east-2.amazonaws.com/wajangchnag'
                }, 
                {
                    'user_id': 2, 
                    'user_nickname': '주펄', 
                    'art_id': 1, 
                    'comment': '평화주의작', 
                    'review_image_url': 'https://upoonbucket.s3.us-east-2.amazonaws.com/innerpeace'
                }]
            }
        )