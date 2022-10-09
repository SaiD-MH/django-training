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

    add_artist = Artist(stageName = 'moksh', socialLink = 'https://www.instagram.com/naruto')
    add_artist.save()

    add_artist = Artist(stageName = 'messi', socialLink = 'https://www.instagram.com/naruto')
    add_artist.save()

    add_artist = Artist(stageName = 'endy', socialLink = 'https://www.instagram.com/naruto')
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
            from albums.models import Album

        - output

            Artist.objects.all().order_by('stageName')
            <QuerySet [<Artist: AmirEid>, <Artist: Mohamed>, <Artist: Naruto>, <Artist: Sayed>, <Artist: Sky>, <Artist: asdasda>, <Artist: endy>, <Artist: messi>, <Artist: moksh>]>

    # list down all artists whose name starts with `a`

        - input

            Artist.objects.filter(stageName__startswith='a')

        - output

            <QuerySet [<Artist: AmirEid>, <Artist: asdasda>]>

    # get the latest released album

        - input
            Album.objects.all().order_by('-release')[0]

        - output
            <Album: barca>



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
            4

    # in 2 different ways, for each artist, list down all of his/her albums

        way1 =>

            input :

            for artist in Artist.objects.all():
                artist.album_set.all()

            output :

                <QuerySet [<Album: Roma>]>
                <QuerySet [<Album: lastDance>]>
                <QuerySet [<Album: GOT>]>
                <QuerySet []>
                <QuerySet []>
                <QuerySet []>
                <QuerySet [<Album: barca>]>
                <QuerySet []>
                <QuerySet []>

        way2 =>

            input :

                for artist in Artist.objects.all():
                         Album.objects.filter(artistName = artist)

            output :

                <QuerySet [<Album: Roma>]>
                <QuerySet [<Album: lastDance>]>
                <QuerySet [<Album: GOT>]>
                <QuerySet []>
                <QuerySet []>
                <QuerySet []>
                <QuerySet [<Album: barca>]>
                <QuerySet []>
                <QuerySet []>



    # list down all albums ordered by cost then by name

        input :
            Album.objects.order_by('cost', 'name')
            Album.objects.order_by('cost', 'name').values()

        output :

            <QuerySet [<Album: lastDance>, <Album: barca>, <Album: Roma>, <Album: GOT>>

            <QuerySet [{'id': 2, 'artistName_id': 2, 'name': 'lastDance', 'creationTime': datetime.datetime(2022, 10, 9, 11, 28,
            28, tzinfo=datetime.timezone.utc), 'release': datetime.datetime(2022, 10, 9, 11, 28, 28, tzinfo=datetime.timezone.utc), 'cost': Decimal('50.170')}, {'id': 4, 'artistName_id': 9, 'name': 'barca', 'creationTime': datetime.datetime(2022, 10, 9, 12, 29, 4, 815586, tzinfo=datetime.timezone.utc), 'release': datetime.datetime(2022, 10, 9, 12, 29, 4, 816157, tzinfo=datetime.timezone.utc), 'cost': Decimal('150.200')}, {'id': 1, 'artistName_id': 1, 'name': 'Roma', 'creationTime': datetime.datetime(2022, 10, 9, 11, 23, 34, tzinfo=datetime.timezone.utc), 'release': datetime.datetime(2022, 10, 9, 11, 23, 34, tzinfo=datetime.timezone.utc), 'cost': Decimal('5000.000')}, {'id': 3, 'artistName_id': 5, 'name':
            'GOT', 'creationTime': datetime.datetime(2022, 10, 9, 11, 52, 29, tzinfo=datetime.timezone.utc), 'release': datetime.datetime(2022, 10, 9, 11, 52, 29, tzinfo=datetime.timezone.utc), 'cost': Decimal('50154.120')}]>
