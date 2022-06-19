from django.contrib import admin
from .models import NeigbourHood,HoodAdmin,HoodUser,Post
# Register your models here.





admin.site.register(HoodAdmin)
admin.site.register(NeigbourHood)
admin.site.register(HoodUser)
admin.site.register(Post)