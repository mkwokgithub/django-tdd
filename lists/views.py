from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request):
    #if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])


    # pass variables from python view code to html templates
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text',''),
        })

