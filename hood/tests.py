from django.test import TestCase
from django.db import models
from .models import HoodUser,Business

@classmethod
def setUpClass(cls):
    user = HoodUser.objects.create(
      username = "user@gmail.com",
      password = "1234"
    )
    user.save()

class TestUser(TestCase):
  #setUp()
 

  def test_init_user(self):
    user = HoodUser.objects.get(username="user@gmail.com")
    self.assertIsInstance(user,HoodUser)
  

class TestBusiness(TestCase):

  def test_bus(self):
    user = HoodUser.objects.get(username="user@gmail.com")
    business = Business.objects.create(name="biz a",user=user)
    self.assertIsInstance(business,Business)


    
  
  
# Create your tests here.
