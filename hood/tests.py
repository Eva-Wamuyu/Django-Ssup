
from django.test import TestCase
from django.db import models
from .models import HoodAdmin, HoodUser,Business,NeigbourHood, Post


# def setUpClass():
#     user = HoodUser.objects.create(
#       username = "user@gmail.com",
#       password = "1234",
#      email ="user@gmail.com",
#     )
#     user.save()

class TestUser(TestCase):
  def setUp(self):
    user = HoodUser.objects.create(
      username = "user@gmail.com",
      password = "1234",
     email ="user@gmail.com",
    )
    user.save()
 

  def test_init_user(self):
    user = HoodUser.objects.get(username="user@gmail.com")
    self.assertIsInstance(user,HoodUser)
  

class TestBusiness(TestCase):
  def setUp(self):
    user = HoodUser.objects.create(
      username = "user@gmail.com",
      password = "1234",
     email ="user@gmail.com",
    )
    user.save()
    new_admin = HoodAdmin.objects.create(phone="1234",title="chief")
    new_admin.save()
    hood = NeigbourHood.objects.create(name="Hood",admin_fk=new_admin)
    business = Business.objects.create(name="biza",user=user,hood=hood)
    business.save()


  def test_bus(self):
    business = Business.objects.get(pk=1)
    self.assertIsInstance(business,Business)

  def test_search(self):
    business = Business.objects.get(pk=1)
    self.assertEqual(len(Business.find_business('biza')),1)

  def test_delete_business(self):
    business = Business.objects.get(pk=1)
    Business.delete_business(business)
    self.assertEqual(len(Business.objects.all()),0)
    

    


    
  
class TestHoodAdmin(TestCase):
  def setUp(self):
    new_admin = HoodAdmin.objects.create(phone="1234",title="chief")
    new_admin.save()
  
  

  def test_admin(self):
    user = HoodAdmin.objects.get(pk=1)
    self.assertIsInstance(user,HoodAdmin)
  
 

class testNeigbourHood(TestCase):
  def setUp(self):
      new_admin = HoodAdmin.objects.create(phone="1234",title="chief")
      new_admin.save()
      hood = NeigbourHood.objects.create(name="Hood",admin_fk=new_admin)
      hood.save()

  def test_admin(self):
    hood = NeigbourHood.objects.get(pk=1)
    self.assertIsInstance(hood,NeigbourHood)



class TestPost(TestCase):

 def Setup(self):
    user = HoodUser.objects.create(
      username = "user@gmail.com",
      password = "1234",
     email ="user@gmail.com",
    )
    user.save()
    new_admin = HoodAdmin.objects.create(phone="1234",title="chief")
    new_admin.save()
    hood = NeigbourHood.objects.create(name="Hood",admin_fk=new_admin)
    new_post = Post(post="abcd",h=hood,user=user)
    new_post.save()


    def test_post(self):
      print("ss")
      post = Post.objects.get(pk=1)
      self.assertIsInstance(post,Post)
      






 




  



# Create your models here.





