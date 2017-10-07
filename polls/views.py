from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.template.loader import render_to_string

@csrf_exempt
def index(request):

    cursor = connections['default'].cursor()
    cursor.execute("SELECT " + \
            "libruary.track_no," + \
            "libruary.artist," + \
            "libruary.track_name," + \
            "genre.name AS genre_name" + \
        " FROM libruary" + \
        " JOIN genre ON (libruary.genre = genre.id)")
    
    rows = dictfetchall(cursor)
    
    result = render_to_string('index.html', {
        'my_string': 'Dima',
        'track_rows': rows
    })
    
    return HttpResponse(result)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]