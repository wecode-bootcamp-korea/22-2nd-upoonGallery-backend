import boto3
import json
import uuid

from django.http  import JsonResponse
from django.views import View

from core.utils     import login_required
from my_settings    import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from arts.models    import Art
from reviews.models import Review, ReviewImage

class ReviewView(View):
    @login_required
    def post(self, request, art_id):
        try:
            user = request.user
            
            if not Art.objects.filter(id=art_id).exists():
                return JsonResponse({"message": "NOT_FOUND"}, status=404)

            review = Review.objects.create(
                user_id = user.id,
                art_id  = art_id,
                comment = request.POST.get("comment")
            )

            s3_client = boto3.client(
                's3',
                aws_access_key_id     = AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY
            )

            image_file      = request.FILES['file']
            image_file_name = str(uuid.uuid1())
            s3_client.upload_fileobj(
                image_file,
                "upoonbucket",
                image_file_name,
                ExtraArgs={
                    "ContentType": image_file.content_type
                }
            )

            image_url = "https://upoonbucket.s3.us-east-2.amazonaws.com/" + image_file_name

            ReviewImage.objects.create(
                review_id = review.id,
                image_url = image_url
            )

            return JsonResponse({'message': 'SUCCESS'}, status=201)
        
        except TypeError:
            return JsonResponse({'message': 'WRONG_TYPE_OBJECT'}, status=400)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEY'}, status=400)    
   
    def get(self, request, art_id):
        reviews = Review.objects.filter(art_id=art_id)
        review_data = [{
            "user_id"         : review.user.id,
            "user_nickname"   : review.user.nick_name,
            "art_id"          : art_id,
            "comment"         : review.comment,
            "review_image_url": review.reviewimage_set.first().image_url if review.reviewimage_set.first() else ""
        } for review in reviews]
        
        return JsonResponse({'message': 'SUCCESS', 'review_data': review_data}, status=200)