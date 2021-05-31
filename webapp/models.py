from django.db import models

# Create your models here.
class userModal(models.Model):
    uid=models.AutoField(primary_key=True)
    firstName=models.CharField(max_length=100)
    lasetName=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    desc=models.TextField(max_length=2000 ,default="" , null=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    profile=models.ImageField(upload_to="upload")
    def __str__(self):
        return str(self.username)
# Create your models here.
class categoryModal(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=100)
    def __str__(self):
        return str(self.cname)

class postModal(models.Model):
    pid=models.AutoField(primary_key=True)
    ptitle=models.CharField(max_length=140)
    pdate=models.DateTimeField(auto_now_add=True)
    pdesc=models.TextField(max_length=2000)
    pthumbnail=models.ImageField(upload_to="upload")
    category=models.ForeignKey(categoryModal,  on_delete=models.SET_NULL , null=True)
    user=models.ForeignKey(userModal,  on_delete=models.SET_NULL , null=True)
    def __str__(self):
        return str(self.ptitle)

