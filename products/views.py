from django import template
from django.shortcuts import render,get_list_or_404,get_object_or_404,redirect
from .models import Product, Category,Quantity,Review,Oreder
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.
def home(request):
    data=Product.objects.order_by('-created_at')[:10]
    category=Category.objects.order_by('-created_at')[:15]
    product=Product.objects.filter(category_relation__in=category).order_by('-created_at').first()
    return render(request,'home.html',{'category': category,'product': product,'data':data})

def all_products(request):
    category=Category.objects.order_by('-created_at')[:15]
    return render(request,'all_products.html',{'category': category})

def product_detail(request,id):
    error=None
    product=get_object_or_404(Product, id=id)
    related_products = Product.objects.filter(category_relation=product.category_relation).exclude(id=product.id).order_by('-created_at')[:4]
    if request.method == 'POST':
        qty = request.POST.get('quantity')
        save_qty = Quantity(qty=qty, product_relation=product)
        save_qty.save()
        messages.success(request, "Your Quantity has been Added successfully!")
        return redirect('product_order', id=id)
    comments = Review.objects.filter(product_relation=product).order_by('-created_at')[:2]
    return render(request,'product_detail_page.html', {'product': product, 'related_products': related_products, 'error': error,'comments': comments})

def product_order(request,id):
    product=get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        review = request.POST.get('review')
        if review:
            product_review = Review(review_text=review, product_relation=product, user_relation=request.user)
            product_review.save()
            return JsonResponse({'error': 'Your review has been submitted successfully!'})
        return redirect('product_order', id=id)
    comments = Review.objects.filter(product_relation=product).order_by('-created_at')[:3]

        
    return render(request,'product_order_page.html',{'product': product, 'comments': comments})

def category_product(request,id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category_relation=category).order_by('-created_at')
    return render(request, 'category/categor_product.html', {'category': category, 'products': products})


def nave_link(request):
    category=Category.objects.order_by('-created_at')[:15]
    return render(request,'nave_link.html',{'category': category})

def order(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        quantity = request.POST.get('quantity')
        total_price = request.POST.get('total_price')
        shipping_address = request.POST.get('shipping_address')
        street = request.POST.get('street')
        phone = request.POST.get('phone')
        if not shipping_address or not street or not phone:
            return JsonResponse({'error': 'Please fill in all required fields.'})
        else:
            order = Oreder(product_relation_id=product_id,user_relation=request.user, quantity=quantity, total_price=total_price, shipping_address=shipping_address, street=street, phone=phone, product_name=product_name)
            order.save()

            return JsonResponse({'error': 'Order placed successfully!'})

    return redirect('product_order')