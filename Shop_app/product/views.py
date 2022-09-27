from django.shortcuts import redirect, render
from .models import Product, Category
from .forms import ProductForm
from django.db.models import Q

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        search = request.POST.get("search")
        results = Product.objects.filter(Q(product_name__icontains=search))

        context = {
        'results' : results

        }

        return render(request, 'products.html', context)

    context = {
        'products' : products,
        'categories' : categories

    }

    return render(request, 'products.html', context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product' : product
    }

    return render(request, 'product_detail.html', context)

def category_detail(request, pk):
    # product = Products.objects.get(pk=pk)
    # context = {
    #     'product' : product
    # }

    # return render(request, 'product_detail.html', context)

    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(product_category=category)
    categories = Category.objects.all()

    if request.method == "POST":
        search = request.POST.get("search")
        results = Product.objects.filter(Q(product_name__icontains=search))

        context1 = {
        'results' : results
        }

        return render(request, 'products.html', context1)

    context = {
        'products' : products,
        'category' : category,
        'categories' : categories
    }
    return render(request, 'category.html', context)

# def blog_like(request, pk):
#     blog = get_object_or_404(Blog, id=request.Products.get('product.pk'))
#     blog.likes.add(request.user)

#     return HttpResponseRedirect(reverse('product-detail'), args=[str(pk)])

def create_product(request):
  form = ProductForm()
  if request.method == "POST":
    form = ProductForm(request.POST, request.FILES)

    if form.is_valid():
        
        form.save()
        return redirect("dash_products")
  
  context = {
    'form' : form
  }

  return render(request, 'create_product.html', context) 

def dash_products(request):
  products = Product.objects.all()

  context = {
    "products" : products,
  }

  return render(request, "dash_products.html", context)

def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, "update_product.html", context)

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('index')

def dynamic_articles_view(request):
    search = Product.objects.filter(product_name__contains='Terry')
    context = {
      'search' : search
    }
    return render(request, "product_detail.html", context)

# def selected_product(request):
#     selected_product = Selected.objects.all()
#     context = {
#         "selected_product" : selected_product
#     }

#     return render(request, "selected_product.html", context)