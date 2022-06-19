from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


# Create your models here.
class HoodUser(AbstractUser):
  name = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  avatar = models.ImageField(upload_to = 'hood',blank=True,default="Awards/avatars_kuiof2.png" )
  hood = models.ForeignKey('NeigbourHood', on_delete=models.CASCADE,null=True)
  email = models.EmailField(unique=True)
  msg = models.CharField(max_length=255, blank=True)
 

class HoodAdmin(models.Model):
  # user = models.ForeignKey(HoodUser, on_delete=models.CASCADE)
  phone = models.BigIntegerField()
  title = models.CharField(max_length=255, null=True)

  def __str__(self):
    return self.title


class NeigbourHood(models.Model):
  admin_fk = models.ForeignKey(HoodAdmin, on_delete=models.CASCADE)
  name = models.CharField(max_length=120)
  location = models.CharField(max_length=120)
  #occupantsCount = models.objects.annotate(occupants = models.Count(''))

  
  def create_neigborhood(self):
    self.save()
  def delete_neigborhood(self):
    self.delete()

  def find_neigborhood(neigborhood_id):
    return NeigbourHood.objects.get(pk=neigborhood_id)

  def update_neighborhood():
    pass
  
  def update_occupants():
    pass

  def __str__(self):
    return self.name





class Business(models.Model):

  class Biz_Types(models.TextChoices):
        FOODS = 'FS', _('Foods')
        CLOTHING = 'CG', _('Clothing')
        CYBER = 'CR', _('Cyber')
        DRINKS = 'DR', _('Drinks')
        GENERAL = 'GR', _('General')

  name = models.CharField(max_length=255)
  user = models.ForeignKey(HoodUser, on_delete=models.CASCADE)
  hood = models.ForeignKey(NeigbourHood,on_delete=models.CASCADE)
  email = models.EmailField()
  biz_type = models.CharField(max_length = 2, choices= Biz_Types.choices,default= Biz_Types.GENERAL)
  avatar = models.ImageField(upload_to = 'hood',null=True,blank=True,default="Awards/avatars_kuiof2.png" )



  @classmethod
  def find_business(cls, search):
    return cls.objects.filter(name__icontains=search).all()

  def create_business(self):
    self.save()
 
  
  def delete_business(self):
    self.delete()

  def update_business(self,pk ,new_business):
    former = Business.object.get(pk=pk)
    former = new_business
    former.save()
    
  

class Post(models.Model):
  post = models.TextField()
  user = models.ForeignKey(HoodUser, on_delete=models.CASCADE)
  date_posted = models.DateTimeField(auto_now=True)
  is_sos = models.BooleanField(default=False)
  h = models.ForeignKey(NeigbourHood,on_delete=models.CASCADE)


 




  



# Create your models here.





