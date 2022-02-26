from importlib.resources import path

from . import views

urlpatterns = [
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name ='product')
]

