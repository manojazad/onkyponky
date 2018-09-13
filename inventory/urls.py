from django.conf.urls import url
from .views import ListAllCategory
from .views import FetchSubCategory
from .views import ProductView


urlpatterns = [
    url('subcategory', FetchSubCategory.as_view()),
    url('category', ListAllCategory.as_view()),
    url('product', ProductView.as_view()),
]