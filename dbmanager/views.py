from django.shortcuts import render
from .models import Article
# Create your views here.

def index(req):
    context = {
        'articles': Article.objects.order_by('id'), # taking all the Article objects from database ordering it by id field
        'title': 'mapage'
    }
    return render(req, 'dbmanager/index.html', context=context)