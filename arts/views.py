from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from arts.models      import Art

class ArtsView(View):
    def get(self,request):
        try:
            shape_name_list  = request.GET.getlist('shape', None) 
            color_name_list  = request.GET.getlist('color', None) 
            theme_name_list  = request.GET.getlist('theme', None)
            min_price        = request.GET.get('min_price', None)
            max_price        = request.GET.get('max_price', None)
            min_size         = request.GET.get('min_size', None)
            max_size         = request.GET.get('max_size', None) 
            artist_name      = request.GET.get('artist', None)
            sort             = request.GET.get('sort', None)
            offset           = int(request.GET.get('offset', 1)) 
            limit            = int(request.GET.get('limit', Art.objects.count()))


            sort_dict = { 
                'id'              : 'id',
                'size-ascend'     : 'size_id', 
                'created-descend' : '-created_at',
                'price-ascend'    : 'price'
            }

            q = Q()

            if artist_name:
                q.add(Q(artist__name = artist_name), q.AND)

            if shape_name_list:
                q.add(Q(shape__name__in = shape_name_list), q.AND)

            if theme_name_list:
                q.add(Q(themes__name__in = theme_name_list), q.AND)

            if color_name_list:
                q.add(Q(colors__name__in = color_name_list), q.AND)

            if min_price and max_price:
                q.add(Q(price__range = (min_price, max_price)), q.AND)

            if min_size and max_size:
                q.add(Q(size__name__range = (min_size, max_size)), q.AND)

            arts = Art.objects.filter(q).distinct().order_by(sort_dict.get(sort, 'id'))
            total_count = arts.count()

            results = [
                {
                'art_id'           : art.id,
                'title'        : art.title,
                'image_url'    : art.image_url,
                'artist_name'  : art.artist.name,
                'artist_id'    : art.artist.id,
                'size'         : art.size.name,
                'is_available' : art.is_available,
                'price'        : art.price,
                'description'  : art.description,
                'shape'        : art.shape.name,
                'price'        : art.price,
                } for art in arts[(offset-1)*limit : (limit*offset)]
            ]
            return JsonResponse({"results": results, "total_count" : total_count}  , status = 200)
        
        except ValueError:
            return JsonResponse({"message" : "VALUE_ERROR"} , status = 400)