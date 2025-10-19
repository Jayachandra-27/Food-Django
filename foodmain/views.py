

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from foodapp.models import Category, Make, Menu
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth



def home(request):
    category=Category.objects.all()
    context={
        'category':category
    }
    return render(request,'home.html',context)


def items(request,pk):
    category = get_object_or_404(Category, pk=pk)
    items = Menu.objects.filter(category=category)
    
    
    context={
        'category':category,
        'items':items
    }
    return render(request,'items.html',context)

def description(request,pk):
    menu_item=get_object_or_404(Menu, pk=pk)
    makes = Make.objects.filter(item_p=menu_item)
    context={
        'menu_item': menu_item,
        'makes': makes
    }
    return render(request,'make.html',context)

def view_menu(request):
    category=Category.objects.all()
    items = Menu.objects.all()
    cart = request.session.get('cart', {})
    
    
    context={
        'category':category,
        'items': items,
        'cart': cart,
        
    }
    return render(request,'view_menu.html',context)


def update_quantity(request, item_id, action):
    # Get the cart from session
    cart = request.session.get('cart', {})  # cart = {item_id: quantity}

    item_id_str = str(item_id)
    current_qty = cart.get(item_id_str, 0)

    if action == 'increase':
        current_qty += 1
    elif action == 'decrease' and current_qty > 0:
        current_qty -= 1

    cart[item_id_str] = current_qty
    request.session['cart'] = cart
    request.session.modified = True # Save back to session

    return redirect('view_menu')

def order_summary(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('view_menu')
    items = []

    for item_id_str, qty in cart.items():
        try:
            item = Menu.objects.get(id=item_id_str)
            item.cart_quantity = qty
            item.total_price = item.price * qty
            items.append(item)
        except Menu.DoesNotExist:
            continue  # skip invalid items

    # Calculate grand total
    grand_total = sum(item.total_price for item in items)

    return render(request, 'order_summary.html', {
        'items': items,
        'grand_total': grand_total
    })


from django.shortcuts import redirect

def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']  # remove cart from session
        request.session.modified = True
    return redirect('home')  # redirect to menu page



def checkout(request):
    if 'cart' in request.session:
        del request.session['cart']
        request.session.modified = True
    

    

    return render(request, 'checkout.html')


def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('dashboard')
    form=AuthenticationForm()
    context={
       'form':form 
    }
    return render(request,'login.html',context)





