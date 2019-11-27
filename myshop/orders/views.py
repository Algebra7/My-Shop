from django.shortcuts import render
from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart

# Create your views here.

def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            
            cart.clear()
            context = {'order': order}
            return render(request, 'orders/order/created.html', context)
    else:
        form = OrderCreateForm()
    context = {'form': form, 'cart': cart}
    return render(request, 'orders/order/create.html', context)