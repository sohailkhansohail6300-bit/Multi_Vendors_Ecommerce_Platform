from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import Q,Sum

from Accounts.models import userprofile

from products.models import Product, Category, Quantity, Oreder
from django.core.paginator import Paginator


def user_profile(request):
    profile = userprofile.objects.get(
        user_profile_relation=request.user
    )

    return render(request, "userProfile/profile.html", {
        "profile": profile
    })


# =========================
# SELLER INVENTORY
# =========================
def seller_inventory(request):
    profile = userprofile.objects.filter(
        user_profile_relation=request.user
    ).first()

    products = Product.objects.filter(
        user_relation=request.user
    ).select_related('category_relation')

    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(Name__icontains=search_query)

    category_filter = request.GET.get('category', '')
    if category_filter:
        products = products.filter(category_relation__id=category_filter)

    # Stock calculation
    for product in products:
        stock = Quantity.objects.filter(
            product_relation=product
        ).aggregate(total=Sum('qty'))

        product.stock_qty = stock['total'] or 0

    paginator = Paginator(products, 10)
    products_page = paginator.get_page(request.GET.get('page', 1))

    categories = Category.objects.all()

    total_products = products.count()
    total_stock = sum(p.stock_qty for p in products)
    low_stock = sum(1 for p in products if 0 < p.stock_qty < 10)
    out_stock = sum(1 for p in products if p.stock_qty == 0)

    # Total seller orders
    new_orders = Oreder.objects.filter(
        product_relation__user_relation=request.user
    ).count()

    return render(request, 'userProfile/product_inventory.html', {
        "profile": profile,
        'products': products_page,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter,
        'total_products': total_products,
        'total_stock': total_stock,
        'low_stock': low_stock,
        'out_stock': out_stock,
        'new_orders': new_orders,  # ← Add this line
    })

# =========================
# ADD PRODUCT
# =========================
def add_product(request):
    profile = userprofile.objects.filter(
        user_profile_relation=request.user
    ).first()

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        description = request.POST.get("description", "").strip()
        price = request.POST.get("price", "").strip()
        category = request.POST.get("category", "").strip()
        qty = request.POST.get("qty", "").strip()
        image = request.FILES.get("image")

        errors = []
        if not name:
            errors.append("Product name is required.")
        if not description:
            errors.append("Product description is required.")
        if not price:
            errors.append("Product price is required.")
        if not category:
            errors.append("Please select a category.")
        if not qty:
            errors.append("Stock quantity is required.")
        if not image:
            errors.append("Please upload a product image.")

        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect("userProfile:add_product")

        product = Product.objects.create(
            Name=name,
            Description=description,
            Price=price,
            image=image,
            category_relation_id=category,
            user_relation=request.user
        )

        Quantity.objects.create(
            product_relation=product,
            qty=qty
        )

        messages.success(request, "Product added successfully.")
        return redirect("userProfile:add_product")

    return render(request, "userProfile/add_product.html", {
        "categories": Category.objects.all(),
        "profile": profile
    })


# =========================
# UPDATE PRODUCT
# =========================
def update_product(request, id):
    profile = userprofile.objects.filter(
        user_profile_relation=request.user
    ).first()

    product = get_object_or_404(
        Product,
        id=id,
        user_relation=request.user
    )

    # Safe quantity lookup
    quantity = Quantity.objects.filter(
        product_relation=product
    ).first()

    if not quantity:
        quantity = Quantity.objects.create(
            product_relation=product,
            qty=0
        )

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        description = request.POST.get("description", "").strip()
        price = request.POST.get("price", "").strip()
        category_id = request.POST.get("category", "").strip()
        qty = request.POST.get("qty", "").strip()
        image = request.FILES.get("image")

        if not all([name, description, price, category_id, qty]):
            messages.error(request, "All fields are required.")
            return redirect("userProfile:update_product", id=id)

        try:
            price = float(price)
            qty = int(qty)
        except ValueError:
            messages.error(request, "Invalid price or quantity.")
            return redirect("userProfile:update_product", id=id)

        category = get_object_or_404(
            Category,
            id=category_id
        )

        product.Name = name
        product.Description = description
        product.Price = price
        product.category_relation = category

        if image:
            product.image = image

        product.save()

        # Update stock quantity
        quantity.qty = qty
        quantity.save()

        messages.success(
            request,
            "Product updated successfully."
        )

        return redirect(
            "userProfile:update_product",
            id=product.id
        )

    return render(
        request,
        "userProfile/update_product.html",
        {
            "profile": profile,
            "product": product,
            "quantity": quantity,
            "categories": Category.objects.all(),
        }
    )


# =========================
# ORDER LIST
# =========================
def order_list(request):
    profile = userprofile.objects.filter(
        user_profile_relation=request.user
    ).first()

    seller_products = Product.objects.filter(
        user_relation=request.user
    )

    orders = Oreder.objects.filter(
        product_relation__in=seller_products
    ).select_related(
        'user_relation',
        'product_relation'
    ).order_by('-created_at')

    search_query = request.GET.get('search', '')

    if search_query:
        orders = orders.filter(
            Q(id__icontains=search_query) |
            Q(user_relation__username__icontains=search_query) |
            Q(user_relation__email__icontains=search_query) |
            Q(product_name__icontains=search_query)
        )

    total_orders = orders.count()

    total_products_sold = (
        orders.aggregate(total=Sum('quantity'))['total'] or 0
    )

    total_revenue = (
        orders.aggregate(total=Sum('total_price'))['total'] or 0
    )

    context = {
        'profile': profile,
        'orders': orders,
        'search_query': search_query,
        'order_stats': {
            'total': total_orders,
            'quantity': total_products_sold,
            'revenue': total_revenue,
        }
    }

    return render(
        request,
        'userProfile/order_list.html',
        context
    )
# =========================
# DELETE PRODUCT (placeholder)
# =========================
def delete_product(request, id):
    product = get_object_or_404(
        Product,
        id=id,
        user_relation=request.user
    )

    product.delete()
    messages.success(request, "Product deleted successfully.")

    return redirect("userProfile:seller_inventory")


def logout(request):
    messages.success(request, "You have been logged out successfully.")
    return redirect('accounts:login')
     
    
    
   