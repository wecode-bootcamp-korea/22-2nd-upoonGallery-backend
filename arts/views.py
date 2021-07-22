from django.views import View
from django.http  import JsonResponse

from arts.models  import Color, Shape, Theme

class CategoryListView(View):
    def get(self,request):
        try:
            themes      = Theme.objects.all()
            theme_list  = [theme.name for theme in themes]
            
            shapes      = Shape.objects.all()
            shape_list  = [shape.name for shape in shapes]
            
            colors      = Color.objects.all()
            color_list  = [color.name for color in colors]
            
            results = [
                {"category_name" : "테마", "category_list" : theme_list},
                {"category_name" : "형태", "category_list" : shape_list},
                {"category_name" : "색상", "category_list" : color_list},
                {"category_name" : "사이즈", "category_list" : ["1~5호", "6~10호","11~15호","16~20호","21~25호","26~30호"]},
                {"category_name" : "구매가격", "category_list" : ["~15만원","15만~30만원","30만~45만원","45만~60만원"]}
            ]
            return JsonResponse({"results": results} , status = 200)
        
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status = 400) 