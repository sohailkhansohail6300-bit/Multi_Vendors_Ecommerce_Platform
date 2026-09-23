


from products.models import Product, Quantity, Oreder
from django.db.models import Sum

def seller_stats(request):
    if not request.user.is_authenticated:
        return {}

    products = Product.objects.filter(
        user_relation=request.user
    )

    low_stock = 0

    for product in products:
        stock = Quantity.objects.filter(
            product_relation=product
        ).aggregate(total=Sum('qty'))['total'] or 0

        if 0 < stock < 10:
            low_stock += 1

    new_orders = Oreder.objects.filter(
        product_relation__user_relation=request.user
    ).count()

    return {
        "new_orders": new_orders,
        "low_stock": low_stock,
    }