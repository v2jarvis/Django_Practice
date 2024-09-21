from django.db import models

# from django.core.exceptions import ValidationError

# Create your models here.


class Students(models.Model):
    """
    Model for student information
    """

    name = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    course = models.CharField(max_length=20)
    mob = models.BigIntegerField()
    addr = models.CharField(max_length=40)

    def __str__(self):
        return str(self.name)


class Contact(models.Model):
    """
    Model for contact information
    """

    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return str(self.message)

    # def clean(self):
    #     if len(self.name)>3 and self.name.isalpha():
    #         return self.name
    #     else:
    #         raise ValidationError({'NameError':'The name should have atleast three letters'})

    # def clean(self):
    #     if '@' in self.email:
    #         return self.email
    #     else:
    #         raise ValidationError({'EmailError':'Enter the valid email id'})

    # def clean(self):
    #     if len(self.course)>1:
    #         return self.course
    #     else:
    #         raise ValidationError({'CourseError':'Enter the valid course name'})

    # def clean(self):
    #     if len(str(self.mob))==10:
    #         return self.mob
    #     else:
    #         raise ValidationError({'MobNumErorr':'Enter the valid mobile number'})

    # def clean(self):
    #     if len(self.addr)>5 and len(self.addr)<20:
    #         return self.addr
    #     else:
    #         raise ValidationError({'AddrError','Enter the valid address'})

    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     return super().save(*args, **kwargs)


# create custom user manager for manage the functionality for abstract user
# class CustomUserManager(BaseUserManager):
#     def create_user(self,email,password=None):
#         if not email:
#             raise ValueError('User must have an email address')
#         user = self.model(
#             email = self.normalize_email(email),

#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,email,password):
#         user = self.create_user(
#             email = self.normalize_email(email),
#             password = password,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# #using abstractuser creation of custom user model
# class User(AbstractUser,PermissionsMixin):
#     username=None
#     email=models.EmailField("email_address",unique=True)

#     USERNAME_FIELD="email"
#     REQUIRED_FIELDS=[]

#     objects=CustomUserManager()

#     def __str__(self):
#         return self.email


# create custom user manager for manage the functionality for abstract user

# class CustomUserManager(BaseUserManager):
#      def _create_user (self, email, password, first_name, last_name, mobile, **extra_fields):
#          if not email:
#              raise ValueError('Users must have an email address')
#          if not password:
#              raise ValueError('Users must have a password')

#          user=self.model(
#              email=self.normalize_email(email),
#              first_name=first_name,
#              last_name=last_name,
#              mobile=mobile
#              **extra_fields)

#          user.set_password(password)
#          user.save(using=self._db)
#          return user

#      def create_user(self,email,password,first_name,last_name,mobile,  **extra_fields):
#         extra_fields.setdefault("is_staff",True)
#         extra_fields.setdefault("is_active",True)
#         extra_fields.setdefault("is_superuser",False)
#         return self._create_user(email,password,first_name,last_name,mobile,**extra_fields)

#      def create_superuser(self,email,password,first_name,last_name,mobile,**extra_fields):
#          extra_fields.setdefault("is_staff",True)
#          extra_fields.setdefault("is_active",True)
#          extra_fields.setdefault("is_superuser",True)
#          return self._create_user(email,password,first_name,last_name,mobile,**extra_fields)


# using abstractbaseuser creation custom user model

# class User(AbstractBaseUser,PermissionsMixin):
#     email = models.EmailField(db_index=True, max_length=254, unique=True)
#     first_name = models.CharField(max_length=240)
#     last_name = models.CharField(max_length=255)
#     mobile = models.CharField(max_length=250)
#     address = models.CharField(max_length=250)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     objects=CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name','last_name','mobile','address']

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'

#     def __str__(self):
#         return self.first_name
