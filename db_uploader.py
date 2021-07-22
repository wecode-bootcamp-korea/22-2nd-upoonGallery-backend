import os, django, csv, sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "upoon_galley.settings")
django.setup()

from users.models   import User
from arts.models    import Art, Artist, Size, Shape, Theme, Color, ArtTheme, ArtColor
from reviews.models import Review, ReviewImage
from carts.models   import Cart

CSV_PATH_PRODUCTS = 'data/users.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)

    for row in data_reader:
        id = row[0]
        email = row[1]
        password = row[2]
        nick_name = row[3]
        birthday = row[4]
        gender = row[5]
        kakao_id = row[6]

        print(id, email, password, nick_name, birthday, gender, kakao_id)

        User.objects.create(
            id = id,
            email = email,
            password = password,
            nick_name = nick_name,
            birthday = birthday,
            gender = gender,
            kakao_id = kakao_id
        )


CSV_PATH_PRODUCTS = 'data/artists.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    
    for row in data_reader:

        id = row[0]
        name = row[1]

        Artist.objects.create(
            id = id,
            name = name
        )

CSV_PATH_PRODUCTS = 'data/sizes.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    
    for row in data_reader:

        id = row[0]
        name = row[1]

        Size.objects.create(
            id = id,
            name = name
        )

CSV_PATH_PRODUCTS = 'data/shapes.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    
    for row in data_reader:

        id = row[0]
        name = row[1]


        Shape.objects.create(
            id = id,
            name = name
        )


CSV_PATH_PRODUCTS = 'data/arts.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)

    artists = {
        '최명준': 1,
        '최현정': 2,
        '김예랑': 3,
        '이종민': 4,
        '이재현': 5,
        '오종택': 6,
        '강경훈': 7,
    }

    shapes = {
        '가로형': 1,
        '세로형': 2,
        '정사각형': 3,
    }

    for row in data_reader:

        id = row[0]
        title = row[1]
        image_url = row[2]
        description = row[3]
        price = row[4]
        artist_id = artists[row[5]]
        size_id = row[6]
        shape_id = shapes[row[7]]
        is_available = row[8]

        print(id, title, image_url, description, price, artist_id, size_id, shape_id, is_available)

        Art.objects.create(
            id = id,
            title = title,
            image_url = image_url,
            description = description,
            price = price,
            artist_id = artist_id,
            size_id = size_id,
            shape_id = shape_id,
            is_available = is_available,
        )


CSV_PATH_PRODUCTS = 'data/colors.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    
    for row in data_reader:

        id = row[0]
        name = row[1]

        print(id, name)

        Color.objects.create(
            id = id,
            name = name
        )

CSV_PATH_PRODUCTS = 'data/themes.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    
    for row in data_reader:

        id = row[0]
        name = row[1]

        print(id, name)

        Theme.objects.create(
            id = id,
            name = name
        )

CSV_PATH_PRODUCTS = 'data/arts_colors.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    
    for row in data_reader:

        id = row[0]
        art_id = row[1]
        color_id = row[2]

        print(id, art_id, color_id)

        ArtColor.objects.create(
            id = id,
            art_id = art_id,
            color_id = color_id
        )

CSV_PATH_PRODUCTS = 'data/arts_themes.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    
    for row in data_reader:

        id = row[0]
        art_id = row[1]
        theme_id = row[2]

        print(id, art_id, theme_id)

        ArtTheme.objects.update_or_create(
            id = id,
            art_id = art_id,
            theme_id = theme_id
        )

CSV_PATH_PRODUCTS = 'data/carts.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    
    for row in data_reader:

        id = row[0]
        user_id = row[1]
        art_id = row[2]

        print(id, user_id, art_id)

        Cart.objects.update_or_create(
            id = id,
            user_id = user_id,
            art_id = art_id
        )

CSV_PATH_PRODUCTS = 'data/reviews.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    
    for row in data_reader:
        id = row[0]
        art_id = row[1]
        comment = row[2]
        user_id = row[3]

        print(id, art_id, comment, user_id)

        Review.objects.update_or_create(
            id = id,
            art_id = art_id,
            comment = comment,
            user_id = user_id
        )

CSV_PATH_PRODUCTS = 'data/reviewimages.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    
    for row in data_reader:
        id = row[0]
        image_url = row[1]
        review_id = row[2]

        print(id, image_url, review_id)

        ReviewImage.objects.update_or_create(
            id = id,
            image_url = image_url,
            review_id = review_id
        )