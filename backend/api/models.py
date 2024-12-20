from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

#payment Status.
status = (
    ("pending", "pending" ),
     ("success", "success" ),
     ("failed", "failed" ),
     ("Refund Initiated", "Refund Initiated"),
     ("Refunded", "Refunded" ),

    )
#transit Status.
transit = (
    ("Ordered", "Ordered" ),
    ("Shipped", "Shipped" ),
     ("In Transit", "In Transit" ),
     ("Delivered", "Delivered" ),
     ("Cancelled", "Cancelled" )

    )
# Custom User Manager..
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, password2 = None, is_farmer=False, is_vendor=False):
        """
        Creates and saves a User with the given email, name, tc,
        password and password2.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name = name,
            is_farmer = is_farmer,
            is_vendor = is_vendor,
   
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email, 
        name and password.
        """
        user = self.create_user(
            email,
            password=password,
            name = name,
         
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
# Custom User Model..
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    is_farmer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
 
class Crop(models.Model):
    # id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length= 100)
    type = models.CharField(max_length= 100)
    desc = models.CharField(max_length= 200)
    image  = models.CharField(max_length= 300)
    price = models.CharField(max_length= 100, default="0")
    quantity = models.IntegerField(default=0)
    lister_email  = models.CharField(max_length= 200, default="admin@gmail.com")
    
    def __str__(self):
        return self.title
    
# class Cart(models.Model):
#     id = models.AutoField(primary_key=True)
#     cust = models.ForeignKey(User, models.CASCADE, default='null')
#     prod = models.ForeignKey(Product, models.CASCADE, default="0")
#     title = models.CharField(max_length= 100)
#     color = models.CharField(max_length= 100)
#     size = models.CharField(max_length= 20)
#     image  = models.CharField(max_length= 400)
#     quantity = models.IntegerField()
#     price = models.CharField(max_length= 100, default="0")
 
   
# class PopularProducts(models.Model):
#     subCategory = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, default="ffsf")
#     category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default="dfd")
#     title = models.CharField(max_length= 100)
#     desc = models.CharField(max_length= 200)
#     color = models.CharField(max_length= 100)
#     size = models.CharField(max_length= 100)
#     image  = models.CharField(max_length= 300)
#     price = models.CharField(max_length= 100, default="0")
#     stockCount = models.IntegerField(default="0")
#     feedback = models.ForeignKey(Feedback., on_delete=models.DO_NOTHING, default="dfd")

    
#     def __str__(self):
#         return self.title

# class Feedback(models.Model):
#     id = models.CharField(max_length=20,  primary_key = True)
#     prod = models.ForeignKey(Product, on_delete=models.CASCADE, default='0')
#     cust = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='0')
#     rating = models.IntegerField(default='0')
#     comment = models.CharField(max_length= 100) 

# class Address(models.Model):
#     id = models.CharField(max_length=20, primary_key = True)
#     cust = models.ForeignKey(User, on_delete=models.CASCADE)
#     mobile = models.CharField(max_length=10, default="999999999")
#     email = models.CharField(max_length=50, default="null")
#     street = models.CharField(max_length=100)
#     landmark = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     pincode = models.CharField(max_length=6)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    farmer_email = models.CharField(max_length=100)
    vendor_email = models.CharField(max_length=100, null=True)   
    crop = models.JSONField()  # Using JSONField to store product list
    date = models.DateTimeField(auto_now_add=True)
    aproved = models.BooleanField(default=False)
    total = models.CharField(max_length=100)   
    paymentMode = models.CharField(max_length=20, null=True)
    paymentStatus = models.CharField(max_length=100, choices=status, default="pending")
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    transit_status =  models.CharField(max_length=20, choices=transit, default="Ordered")