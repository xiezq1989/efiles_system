from django.db import models

# Create your models here.
class Upload(models.Model):
    user_name = models.CharField(max_length = 50)
    title_name=models.CharField(max_length = 150,blank=True)
    file_size=models.IntegerField(blank=True,null=True)
    created_time=models.DateTimeField(auto_now_add=True)  # auto_now_add: admin also can't change the create time
    update_time=models.DateTimeField(auto_now=True)       # auto_now: admin also can't change the update time
    file_url = models.FileField(upload_to = './%Y%m')