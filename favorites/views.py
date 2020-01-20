from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from favorites.models import Favorite


@login_required()
def favorite_save(request):
    if request.method == "POST":
        substitute_code = int(request.POST.get("substitute-code"))
        product_code = int(request.POST.get("product-code"))
        substitute = Product.objects.get(code=substitute_code)
        product = Product.objects.get(code=product_code)

        if substitute and product:
            Favorite.objects.get_or_create(user=request.user, product=product, substitute=substitute)

        return redirect("product_info", substitute_code)

    return redirect("home")