from django.contrib import admin
from .models import DishCategory, Dish, About, Service,Gallery,Reservation
# Register your models here.
#admin.site.register(DishCategory)
#admin.site.register(Dish)

# admin.site.register(About)
# admin.site.register(Service)
# admin.site.register(Gallery)

admin.site.register(Reservation)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display =['heading', 'desc_history']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display =['title','desc', 'is_visible', 'icon']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

@admin.register(Dish) # Реєструємо модель Діш
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','position', 'is_visible', 'is_special', 'is_signature', 'price',
                    'discount', 'ingredients','photo' ]
    list_filter = ['is_visible', 'is_special', 'is_signature', 'category']
    list_editable = [ 'category','position', 'is_visible', 'is_special', 'is_signature',  'price',
                    'discount', 'ingredients','photo']


# @admin.register(DishCategory) # Назва моделі для якої буде працювати ця адмінка
# class DishCategoryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'position', 'is_visible']
#     list_filter = ['is_visible']
#     list_editable = ['position', 'is_visible']

class DishInline(admin.TabularInline):
    model = Dish

# Візуалізація категорії сніданки в адмінці
@admin.register(DishCategory) # Назва моделі для якої буде працювати ця адмінка
class CategoriesWithDishesAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible']
    list_filter = ['is_visible']
    list_editable = ['position', 'is_visible']
    inlines = [DishInline]