from django.contrib import admin
from .models import User, Crop
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserModelAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'name','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ()   
    
admin.site.register(User, UserModelAdmin) 

   
class CropAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'quantity', 'lister_email', 'desc')
    
admin.site.register(Crop, CropAdmin)     
    
# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category')    
   
# admin.site.register(SubCategory, SubCategoryAdmin) 

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'color', 'size', 'desc')
   
# admin.site.register(Product, ProductAdmin) 

# class CartAdmin(admin.ModelAdmin):
#     list_display = ('id','prod_id', 'cust_id', 'title', 'color', 'size', 'price', 'quantity')
   
# admin.site.register(Cart, CartAdmin) 

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'crop','vendor_email', 'farmer_email', 'approved', 'total', 'transit_status')
   
# admin.site.register(OrderSummary, OrderSummaryAdmin)

# class FeedbackAdmin(admin.ModelAdmin):
#     list_display = ('id', 'cust_id', 'prod_id', 'rating', 'comment')
   
# admin.site.register(Feedback, FeedbackAdmin) 

# class AddressAdmin(admin.ModelAdmin):
#     list_display = ('id', 'cust_id', 'street', 'city', 'state', 'pincode')
   
# admin.site.register(Address, AddressAdmin)

