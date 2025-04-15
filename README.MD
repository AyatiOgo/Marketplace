# ABOUT MY ECCORMERCE PROJECT
This project was created with django. In this project I learnt how to
1. Serve static files 
2. Serve Staticfiles using whitenoise
3. My code for deployment
4. Deploy to vercel 
5. The use of gunicorn and Procfiles
6. The use of .env files
7. How to use dot env 
8. How to use github 
9. How to migrate to an external database
10. How to link to static images to display in my app
11. I learnt about pyscorpg2-binary for database 
12. I learnt how to use cloudinary to handle my images
13. I learnt how to properly push to github 
14. I learnt the use of requirement.txt in deployment
15. I learnt to structure my django app properly to avoid errors in deployment
16. And now I'm learing how to create Readme files

## My key takeaways from this 
    - keep practicing
    - Don't let errors dicourage you
    - it's okay to start again
    - have a good tutor 
    - coding is actually fun! 😁


## Below are some screenshots of my project

1. The Home page
![Homepage](/market/screenshots/pic-1.png)

2. The Product lists
![Products](/market/screenshots/pic-2.png)

3. Product page 
![Product-page](/market/screenshots/pic-4.png)

4. Extra stuffs
![extras](/market/screenshots/pic-3.png)



#### Below is code for views 
```python 
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def view_products(request):
    products = Product.objects.all()

    context = {"products" : products}

    return render(request, "product-list.html", context)


def product_page(request, id):
    product = get_object_or_404(Product, id=id)

    context = {'product': product}

    return render(request, "product-page.html", context)

```