from django.contrib import admin

list_display = ['id', 'name', 'image', 'price', 'release_date','lte_exists',]
list_filter = ['name', 'price',]
