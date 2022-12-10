from django.shortcuts import render
from django.views.generic import DeleteView, CreateView, TemplateView, UpdateView, DetailView, ListView, FormView
from django.urls import reverse_lazy
from . import models, forms
from books import models as book_models
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin



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
        context = context,
        
    )


class DelPosition(UserPassesTestMixin, DeleteView):
    model = models.BookInCart
    success_url = reverse_lazy('orders:show-cart')
    template_name='orders/position_delete.html'
    def test_func(self):
        cart_id = self.request.session.get('cart_id')
        cart = models.Cart.objects.get(pk=cart_id)
        the_good_to_be_deleted = self.get_object() #objects_list если много объектов
        goods = cart.books.filter(pk=the_good_to_be_deleted.pk) #товары в корзинке, выборка
        return goods

class UpdatePosition(UpdateView):
    model = models.BookInCart
    success_url = reverse_lazy('orders:show-cart')
    fields = ('quantity',)



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

class OrderDetail(LoginRequiredMixin, DetailView):
    template_name = 'orders/detail-order.html'
    model = models.Order
    login_url = reverse_lazy('login')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['url_update_order'] = 'orders:update-order'
        context['url_update_bic'] = 'orders:update-bic'
        context['form'] = forms.OrderCommentForm
        order_pk = self.object.pk
        context['comments'] = models.OrderComment.objects.filter(order__pk=order_pk).all()
        return context

class OrderList(LoginRequiredMixin, ListView):
    model = models.Order
    template_name = 'orders/list-order.html'
    login_url = reverse_lazy('login')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['my_orders'] = models.Order.objects.filter(cart__user=self.request.user)
        # context['my_orders_not_done'] = models.Order.objects.filter(cart__user=self.request.user).exclude(status__name="Done")
        #context['my_orders_done'] = models.Order.objects.filter(cart__user=self.request.user, status__name="Done")
        # context['my_orders_commented'] = models.Order.objects.select_related('order_comment').filter(cart__user=self.request.user, status__name="Done")
        context['url_delete_name'] = 'orders:delete-order'
        context['url_detail_name'] = 'orders:detail-order'
        # context['form'] = forms.OrderCommentForm
        return context

class OrderAllList(LoginRequiredMixin, ListView):
    model = models.Order
    template_name = 'orders/list-all-order.html'
    login_url = reverse_lazy('login')
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['all_orders'] = models.Order.objects.order_by('-created_date').all()
        context['url_detail_name'] = 'orders:detail-order'
        context['url_update_name'] = 'orders:update-order'
        return context

class DelOrder(LoginRequiredMixin, DeleteView):
    model = models.Order
    success_url = reverse_lazy('orders:list-order')
    template_name='orders/order_delete.html'
    login_url = reverse_lazy('login')

class UpdateOrder(UpdateView):
    model = models.Order
    form_class = forms.OrderUpdateForm
    template_name = 'orders/order_update.html'
    success_url = reverse_lazy('orders:list-order')



class UpdateBookInCart(UpdateView):
    model = models.BookInCart
    form_class = forms.BookInCartForm
    template_name = 'orders/order_update.html'
    success_url = reverse_lazy('orders:list-order')

class CreateOrderComment(LoginRequiredMixin, CreateView):
    model = models.OrderComment
    template_name = 'orders/create-comment.html'
    form_class = forms.OrderCommentForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('orders:order-success')
    success_url = reverse_lazy('orders:list-order')

    def form_valid(self, form):
        order_pk = self.request.POST.get('order_pk')
        print(order_pk)
        order=models.Order.objects.get(pk=order_pk)
        form.instance.order = order
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('orders:detail-order', kwargs={'pk': self.object.order.pk})

class OrderCommentSuccess(TemplateView):
    template_name = 'orders/comment-success-order.html'

# class ListOrderComment(ListView):
#     model = models.OrderComment
#     template_name = 'orders/comments_list.html'
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['operation_name'] = 'List of Comments'
#         context['comments'] = models.OrderComment.objects.filter(pk=self.request.get.pk).all
#         # context['url_delete_name'] = 'books:book-delete'
#         # context['url_create_name'] = 'books:book-create'
#         # context['url_detail_name'] = 'books:book-detail'
#         # context['operation_for_add'] = 'Add new Book'
#         return context

