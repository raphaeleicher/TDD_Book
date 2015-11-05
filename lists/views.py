from django.shortcuts import render, redirect
from lists.models import Item

# ToDo: Support more than one list!


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    else:
        return render(request, 'lists/home.html')
