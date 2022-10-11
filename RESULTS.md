    #Tasks

    * create some artists
    * list down all artists
    * list down all artists sorted by name
    * list down all artists whose name starts with `a`
    * in 2 different ways, create some albums and assign them to any artists
    * get the latest released album
    * get all albums released before today
    * get all albums released today or before but not after today
    * count the total number of albums (hint: count in an optimized manner)
    * in 2 different ways, for each artist, list down all of his/her albums
    * list down all albums ordered by cost then by name (cost has the higher priority)


    #all imported models

        - from artists.models import Artist
        - from albums.models import Album
        - from datetime import datetime



    # create some artist

    add_artist = Artist(stageName = 'moksh', socialMediaProfile = 'https://www.instagram.com/naruto')
    add_artist.save()

    add_artist = Artist(stageName = 'messi', socialMediaProfile = 'https://www.instagram.com/naruto')
    add_artist.save()

    add_artist = Artist(stageName = 'endy', socialMediaProfile = 'https://www.instagram.com/naruto')
    add_artist.save()



    # list down all artists

        - input
            Artist.objects.all()

        - output
            <QuerySet [<Artist: AmirEid>, <Artist: Mohamed>, <Artist: Naruto>, <Artist: Sayed>, <Artist: Sky>, <Artist: asdasda>, <Artist: endy>, <Artist: messi>, <Artist: moksh>]>

    # create some album

        addAlbum=Album(artistName = add_artist, name = 'barca' ,cost = 150.200)
        addAlbum.save()

    # list down all artists sorted by name


        - input
            Artist.objects.all().order_by('stageName')

        - output

            
            <QuerySet [<Artist: amir.eid>, <Artist: deadSouls>, <Artist: endy>, <Artist: messi>, <Artist: moksh>]>

    # list down all artists whose name starts with `a`

        - input

            Artist.objects.filter(stageName__startswith='a')

        - output

            <QuerySet [<Artist: amir.eid>]>

    # get the latest released album

        - input
            Album.objects.all().order_by('-release')[0]

        - output
            <Album: Home>



    # get all albums released before today

        - input
            Album.objects.filter(release__lt = datetime.today().date())
        - output
            <QuerySet []>

    # get all albums released today or before but not after today
        - input
            Album.objects.filter(release__lte = datetime.today().date())
        - output
            <QuerySet []>
    # count the total number of albums

        - input
            Album.objects.all().count()
        - output
            5

    # in 2 different ways, for each artist, list down all of his/her albums

        way1 =>

            input :

            for artist in Artist.objects.all():
                artist.album_set.all()

            output :

                <QuerySet []>
                <QuerySet [<Album: Roma>]>
                <QuerySet [<Album: barca>, <Album: Home>]>
                <QuerySet [<Album: Help>]>
                <QuerySet [<Album: uzumaki>]>

        way2 =>

            input :

                for artist in Artist.objects.all():
                         Album.objects.filter(artistName = artist)

            output :

                <QuerySet []>
                <QuerySet [<Album: Roma>]>
                <QuerySet [<Album: barca>, <Album: Home>]>
                <QuerySet [<Album: Help>]>
                <QuerySet [<Album: uzumaki>]>



    # list down all albums ordered by cost then by name

        input :
            Album.objects.order_by('cost', 'name')
            Album.objects.order_by('cost', 'name').values()

        output :

            <QuerySet [<Album: barca>, <Album: Roma>, <Album: Home>, <Album: uzumaki>, <Album: Help>]>

            <QuerySet [{'id': 2, 'name': 'barca', 'artistName_id': 4, 'creationTime': datetime.datetime(2022, 10, 11, 19, 29, 19, 49734, tzinfo=datetime.timezone.utc), 'release': datetime.datetime(2022, 10, 11, 19, 29, 19, 49734, tzinfo=datetime.timezone.utc), 'cost': Decimal('150.20000')}, {'id': 1, 'name': 'Roma', 'artistName_id': 1, 'creationTime': datetime.datetime(2022, 10, 11, 19, 12, 48, tzinfo=datetime.timezone.utc), 'release': datetime.datetime(2022, 10, 11, 19, 12, 
            48, tzinfo=datetime.timezone.utc), 'cost': Decimal('500.50000')}, {'id': 5, 'name': 'Home', 'artistName_id': 4, 'creationTime': datetime.datetime(2022, 10, 11, 19, 37, 6, tzinfo=datetime.timezone.utc), 'release': datetime.datetime(2022, 10, 11, 19, 37, 6, tzinfo=datetime.timezone.utc), 'cost': Decimal('784.10000')}, {'id': 3, 'name': 'uzumaki', 'artistName_id': 2, 'creationTime': datetime.datetime(2022, 10, 11, 19, 36, 6, tzinfo=datetime.timezone.utc), 'release': 
            datetime.datetime(2022, 10, 11, 19, 36, 6, tzinfo=datetime.timezone.utc), 'cost': Decimal('4784.12000')}, {'id': 4, 'name': 'Help', 'artistName_id': 3, 'creationTime': datetime.datetime(2022, 10, 11, 19, 36, 38, tzinfo=datetime.timezone.utc), 'release': datetime.datetime(2022, 10, 11, 19, 36, 38, tzinfo=datetime.timezone.utc), 'cost': Decimal('5454.77000')}]>
