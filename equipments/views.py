from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from equipments.models import Items, ItemDetails
from plants.models import Cart
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def checkout(request):
    templates=loader.get_template('echeckout.html')
    current_user = request.user.id
    cart = Cart.objects.all().filter(id_user=current_user).first()
    product=Items.objects.get(id=cart.id_product)
    context={
        'cart':cart,
        'productname': product,
        'request': request
    }
    return HttpResponse(templates.render(context))

def add_to_cart(request, id):
    currentuser=request.user
    discount=2
    status=False
    equipment=ItemDetails.objects.select_related('itemsid').filter(id=id)
    count=0
    for item in equipment:
        net=item.total-discount
        count=count+1
    cart= Cart(
      id_product=item.id,
      id_user=currentuser.id,
      price=item.price,
      qty=item.qty,
      tax=item.tax,
      total=item.total,
      discount=discount,
      image=item.image,
      net=net,
      status=status
    )
    currentuser=request.user.id
    count=Cart.objects.filter(id_user=currentuser).count()
    cart.save()
    request.session['countcart']=count
    return redirect('/showequipments')

def showequipments(request):
    templates=loader.get_template('showequipments.html')
    equipment=ItemDetails.objects.select_related('itemsid')
    return HttpResponse(templates.render({'equip':equipment, 'request': request}))

def edetails(request, id):
    template=loader.get_template('edetails.html')
    equipment=ItemDetails.objects.select_related('itemsid').filter(id=id)
    print(equipment)
    
    context={
        'equip':equipment,
        'request': request
    }
    return HttpResponse(template.render(context))