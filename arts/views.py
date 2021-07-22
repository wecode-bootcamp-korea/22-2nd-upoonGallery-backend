from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from arts.models      import Art, Artist

class ArtsFilterView(View):
    def get(self,request):

        artist_name      = request.GET.get('artist', None)   
        shape_name_list  = request.GET.getlist('shape', None) 
        size_name_list   = request.GET.getlist('size' , None) 
        color_name_list  = request.GET.getlist('color', None) 
        theme_name_list  = request.GET.getlist('theme', None)
        price_list       = request.GET.getlist('price', None)
        
        if artist_name:
            arts = Artist.objects.get(name = artist_name).art_set.all()
            results = [art.image_url for art in arts]

            return JsonResponse({"results": results} , status = 200)
        
        q_shape = Q() 
        for shape_name in shape_name_list:
            q_shape.add(Q(shape__name = shape_name), q_shape.OR)
        
        q_size = Q()
        for size in size_name_list:
            size = int(size) * 10
            q_size.add(Q(size__name__gt = (size-10)) & Q(size__name__lte= size),q_size.OR)

        q_color = Q()
        for color in color_name_list:
            q_color.add(Q(colors__name = color), q_color.OR)

        q_theme = Q()
        for theme in theme_name_list:
            q_theme.add(Q(themes__name = theme), q_theme.OR)

        q_price = Q()
        for price in price_list:
            price = int(price) * 150000
            q_price.add(Q(price__gt = (price-150000)) & Q(price__lte= price),q_price.OR)

        q = Q()
        q= (q_shape & q_size & q_color & q_theme & q_price)
    
        arts = Art.objects.filter(q)
        results = [
            {
            'id'          : art.id,
            'title'       : art.title,
            'image_url'   : art.image_url,
            'artist_name' : art.artist.name,
            'size'        : art.size.name
            } for art in arts
        ]

        return JsonResponse({"results": results[:10], "total_count": len(results)} , status = 200)
