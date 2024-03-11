from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Items, ItemDetails, Cart
from django.contrib.auth import login, logout, authenticate
from .forms import CreateUserForm , LoginUserForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
#from rest_framework.decorators import api_view


# Create your views here.
#@api_view(['GET'])
@login_required()
def checkout(request):
    templates=loader.get_template('checkout.html')
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
    plant=ItemDetails.objects.select_related('itemsid').filter(id=id)
    count=0
    for item in plant:
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
    return redirect('/insideplants')

def home(request):
    templates=loader.get_template('plantsindex.html')
    return HttpResponse(templates.render({'request': request}))

def showinsideplants(request):
    templates=loader.get_template('insideplants.html')
    plant=ItemDetails.objects.select_related('itemsid')
    return HttpResponse(templates.render({'plant':plant, 'request': request}))

def details(request, id):
    template=loader.get_template('details.html')
    plant=ItemDetails.objects.select_related('itemsid').filter(id=id)
    context={
        'plant':plant,
        'request': request
    }
    return HttpResponse(template.render(context))


@csrf_exempt
def auth_register(request):
    templates=loader.get_template('auth_register.html')
    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_login')
    context={'registerform': form}
    return HttpResponse(templates.render(context=context))

@csrf_exempt
def auth_login(request):
    form=LoginUserForm()
    if request.method=='POST':
        form=LoginUserForm(data=request.POST)
        if form.is_valid():
           username=form.cleaned_data['username']
           password=form.cleaned_data['password']

           user=authenticate(username=username,password=password)
           if user:
               if user.is_active:
                  login(request,user)
                  return render(request,'plantsindex.html')
    context={'form': form}
    return render(request, 'auth_login.html', context)

@csrf_exempt
def auth_logout(request):
   if request.method=='POST':
       logout(request)
       return redirect("/")