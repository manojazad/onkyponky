# Onkyponky

1) API to get all categories<br/>
http://127.0.0.1:8000/inventory/category

2) API to get subcategories for a category<br/>
http://127.0.0.1:8000/inventory/subcategory?id=2

3) API to get all products for a category<br/>
http://127.0.0.1:8000/inventory/product?cat=2

4) API to get all products for a subcategory<br/>
http://127.0.0.1:8000/inventory/product?subcat=4

5) API to post new product under existing subcategory and category<br/>
curl -X POST http://127.0.0.1:8000/inventory/product -H 'Content-Type: application/json' -d '{"name": "Iphone X", "category": 1, "subCategory": 4}'
