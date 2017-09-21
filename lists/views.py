from django.http import HttpResponse
from django.shortcuts import render
from lists.models import Item


# Create your views here.


def home_page(request):

    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
    else:
        new_item_text = ''
    
    #if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])


    # pass variables from python view code to html templates
    return render(request, 'home.html', {
        'new_item_text': new_item_text
        })

