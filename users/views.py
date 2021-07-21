import json, requests, jwt

from django.http      import JsonResponse
from django.views     import View

from users.models import User

from my_settings import SECRET_KEY, ALGORITHM

class KakaoSignInView(View):
    def get(self, request):
        try:
            kakao_access_token = request.headers.get('Authorization')

            headers = {'Authorization': f'Bearer {kakao_access_token}'}

            kakao_user_info = requests.post('https://kapi.kakao.com/v2/user/me', headers=headers).json()

            kakao_id  = kakao_user_info['id']
            email     = kakao_user_info['kakao_account']['email']
            nick_name = kakao_user_info['properties']['nickname']
            birthday  = kakao_user_info['kakao_account']['birthday']
            gender    = kakao_user_info['kakao_account']['gender']

            user, is_created =  User.objects.get_or_create(kakao_id = kakao_id)
            
            if is_created:
                user.email     = email
                user.nick_name = nick_name
                user.birthday  = birthday
                user.gender    = gender
                user.save()

            access_token = jwt.encode({'user_id': user.id}, SECRET_KEY, algorithm=ALGORITHM)

            return JsonResponse({'access_token': access_token}, status=200)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Exception as error:
            return JsonResponse({'message': error}, status=400)