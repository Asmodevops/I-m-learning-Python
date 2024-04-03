from django.urls import path, re_path

import pets.views as pets

urlpatterns = [
    path('', pets.index, name='main_url'), # pets = http://127.0.0.1:8000/pets/
    # path('cats/', pets.cats), # http://127.0.0.1:8000/pets/cats
    # path('dogs/', pets.dogs), # http://127.0.0.1:8000/pets/dogs
    path('<slug:pet_slug>/', pets.pet), # http://127.0.0.1:8000/pets/{pet_slug}
    path('categories/<int:categ_id>/', pets.categories), # http://127.0.0.1:8000/pets/{int}
]

