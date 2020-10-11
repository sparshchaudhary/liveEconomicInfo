from django.db import models

# Create your models here.

class GovJobPost (models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    slug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="Index/images", default="")
    created_on = models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' ---- by ----  ' + self.category

class BookPost (models.Model):
    sno = models.AutoField(primary_key=True)

    BookOneName = models.CharField(max_length=150)
    BookOneUrl = models.URLField(max_length=500)

    BookTwoName = models.CharField(max_length=150)
    BookTwoUrl = models.URLField(max_length=500)

    BookThreeName = models.CharField(max_length=150)
    BookThreeUrl = models.URLField(max_length=500)

    BookFourName = models.CharField(max_length=150)
    BookFourUrl = models.URLField(max_length=500)

    BookFiveName = models.CharField(max_length=150)
    BookFiveUrl = models.URLField(max_length=500)

    BookSixName = models.CharField(max_length=150)
    BookSixUrl = models.URLField(max_length=500)

