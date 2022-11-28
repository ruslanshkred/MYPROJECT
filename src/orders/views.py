from django.shortcuts import render
from django.views.generic import DeleteView, CreateView, TemplateView
from django.urls import reverse_lazy
from . import models, forms
from books import models as book_models
from django.contrib.auth.mixins import UserPassesTestMixin



def show_cart(request):
    context = {}
    context['cart'] = None
    if request.method == 'POST':
        book_pk = request.POST.get('book_pk')
        quantity = int(request.POST.get('quantity'))
        if book_pk and quantity:
            cart_id = int(request.session.get('cart_id', 0))
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None
            if cart_id == 0:
                cart_id = None
            cart, created = models.Cart.objects.get_or_create(
                pk = cart_id,
                defaults = {'user': user}
            )
            context['cart'] = cart
            if created:
                request.session['cart_id'] = cart.pk

            book = book_models.Book.objects.get(pk=int(book_pk))
            price = book_models.Book.objects.get(pk=int(book_pk))
            book_in_cart, created = models.BookInCart.objects.get_or_create(
                book=book,
                cart=cart,
                defaults={
                    'quantity':quantity,
                    'price':price, 
                }
            )
            if not created:
                book_in_cart.quantity = book_in_cart.quantity + quantity
                book_in_cart.save()

    else:
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = models.Cart.objects.get(pk=cart_id)
            context['cart'] = cart
    context['form'] = forms.OrderForm

    return render(
        request = request,
        template_name='orders/view_cart.html',
        context = context
    )


class DelPosition(DeleteView):
    model = models.BookInCart
    success_url = reverse_lazy('orders:show-cart')
    template_name='orders/position_delete.html'
    # def test_func(request):
    #     book_in_cart = models.BookInCart.objects.get(pk=id)
    #     cart_id = request.session.get('cart_id')
    #     if cart_id == book_in_cart.id
    #     book_in_cart == request.session.pk
    #      = request.POST.get('book_in_cart')
    #     return self.id == int(self.request.session.cart_id)
#        return self.request.user == self.request.session.cart_pk

class Order(CreateView):
    template_name = 'orders/create_order.html'
    model = models.Order
    form_class = forms.OrderForm
    success_url = reverse_lazy('orders:order-success')

    def form_valid(self, form):
        cart=models.Cart.objects.get(pk=self.request.session.get('cart_id'))
        form.instance.cart = cart
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        del self.request.session['cart_id']
        return super().get_success_url()

class OrderSuccess(TemplateView):
    template_name = 'orders/success-order.html'