from . import views
from django.urls import path


urlpatterns = [
path('login/',views.logger,name="logger"),
path('signup/',views.signer,name="signer"),
path('',views.index,name="index"),
path('home/',views.home,name="home"),
path('news/',views.news,name="news"),
path('profile/',views.profile,name="profile"),
path('post/',views.post,name="post"),
path('settings/',views.settings,name="settings"),
path('del/<item>/<int:id>',views.delete,name="delete"),
path('logout/',views.loggout,name="logout"),



]