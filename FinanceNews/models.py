from django.db import models

# Create your models here.

class LatestFinancenewspost (models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=20)
    Fslug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="FinanceNews/Postimages", default="")
    created_on = models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' ---- by ----  ' + self.author

class SideNewsPics (models.Model):
    sno = models.AutoField(primary_key=True)
    SideNewsImage1 = models.ImageField(upload_to="Index/images", default="")
    SideNewsImage2 = models.ImageField(upload_to="Index/images", default="")
    SideNewsImage3 = models.ImageField(upload_to="Index/images", default="")

class HeaderNewsPics (models.Model):
    sno = models.AutoField(primary_key=True)
    HeaderNewsImage1 = models.ImageField(upload_to="Index/images", default="")
    HeaderNewsImage2 = models.ImageField(upload_to="Index/images", default="")
    HeaderNewsImage3 = models.ImageField(upload_to="Index/images", default="")





    