from django.db import models

# Create your models here.

class Post(models.Model):
    description = models.CharField(max_length=20)
    #image = models.ImageField(upload_to='path', blank=True)
    slug = models.SlugField()
    tag = models.CharField(max_length=20)
    author = models.ForeignKey(User, unique=True)
    image = models.ImageField(upload_to='path', 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    read_time =  models.IntegerField(default=0)       # models.TimeField(null=True, blank=True) #assume minutes
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def isVerified():
        return User__isVerified()

    def isOrganisation():
        return User__isOrganisation()

    def isValid():
        return User__isValid()
        
    
    
    