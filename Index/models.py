from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' +  self.name + ' - ' + self.email

class IndexPageStockContact (models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    useremail = models.CharField(max_length=50)
    userphone = models.CharField(max_length=15)

    def __str__(self):
        return 'Message from  --- ' +  self.username + '--- ' + self.useremail 

class IndexValue(models.Model):
    sno = models.AutoField(primary_key=True)
    niftyvalue = models.TextField()
    sensexvalue = models.TextField()
    timeStamp = models.DateTimeField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.niftyvalue + ' --- '  + ' Index Value'

class StockDetails (models.Model):
    sno = models.AutoField(primary_key=True)
    stockofweekshare = models.TextField()
    stockofweeksharedetail = models.TextField()
    stockofweektimeStamp = models.DateTimeField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    stockofmonthshare = models.TextField()
    stockofmonthsharedetail = models.TextField()
    stockofmonthtimeStamp = models.DateTimeField(blank=True)
    hrhrshare = models.TextField()
    hrhrsharedetail = models.TextField()
    hrhrsharetimeStamp = models.DateTimeField(blank=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.stockofweekshare + ' ---- ' + ' Post Weekly '

class IndexJobPost (models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=20)
    testslug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="Index/images", default="")
    created_on = models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' ---   by  ---  ' + self.author

class IndexNewsPost (models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=20)
    slug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="Index/images", default="")
    created_on = models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' ---  by ---  ' + self.author

class IndexOtherPosts (models.Model):
    sno = models.AutoField(primary_key=True)
	
    Globalheading = models.CharField(max_length=150)
    Globalcontent = models.TextField()
    Globalimage = models.ImageField(upload_to="Index/images", default="")
    GlobaltimeStamp = models.DateTimeField(default=0, blank=True)  

    Currencyheading = models.CharField(max_length=150)
    Currencycontent = models.TextField()
    Currencyimage = models.ImageField(upload_to="Index/images", default="")
    CurrencytimeStamp = models.DateTimeField(default=0, blank=True)  
	
    Comoditiesheading = models.CharField(max_length=150)
    Comoditiescontent = models.TextField()
    Comoditiesimage = models.ImageField(upload_to="Index/images", default="")
    ComoditiestimeStamp = models.DateTimeField(default=0, blank=True)  
	
    Otherheading = models.CharField(max_length=150)
    Othercontent = models.TextField()
    Otherimage = models.ImageField(upload_to="Index/images", default="")
    OthertimeStamp = models.DateTimeField(default=0, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.Globalheading

class StockOfTheWeek (models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    sector = models.CharField(max_length=20)
    # slug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="Index/images", default="")
    created_on = models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' ---   by  ---  ' + self.sector

class StockOfTheMonth (models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    sector = models.CharField(max_length=20)
    # slug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="Index/images", default="")
    created_on = models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' ---   by  ---  ' + self.sector

class HighRiskHighReturn (models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    sector = models.CharField(max_length=20)
    # slug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="Index/images", default="")
    created_on = models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' ---   by  ---  ' + self.sector

class BookStore (models.Model):
    sno = models.AutoField(primary_key=True)
	
    BookOneName = models.CharField(max_length=150)
    BookOneUrl = models.URLField(max_length=500)
    # BookOneImage = models.ImageField(upload_to="Index/images", default="")

    BookTwoName = models.CharField(max_length=150)
    BookTwoUrl = models.URLField(max_length=500)
    # BookTwoImage = models.ImageField(upload_to="Index/images", default="")
	
    BookThreeName = models.CharField(max_length=150)
    BookThreeUrl = models.URLField(max_length=500)
    # BookThreeImage = models.ImageField(upload_to="Index/images", default="")

    BookFourName = models.CharField(max_length=150)
    BookFourUrl = models.URLField(max_length=500)
    # BookThreeImage = models.ImageField(upload_to="Index/images", default="")

    BookFiveName = models.CharField(max_length=150)
    BookFiveUrl = models.URLField(max_length=500)
    # BookThreeImage = models.ImageField(upload_to="Index/images", default="")

    BookSixName = models.CharField(max_length=150)
    BookSixUrl = models.URLField(max_length=500)
    # BookThreeImage = models.ImageField(upload_to="Index/images", default="")
	
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.BookOneName + '--- Index Book Stor ---'

class NewsPic (models.Model):
    sno = models.AutoField(primary_key=True)
    NewsImage1 = models.ImageField(upload_to="Index/images", default="")
    NewsImage2 = models.ImageField(upload_to="Index/images", default="")
    NewsImage3 = models.ImageField(upload_to="Index/images", default="")

class IndexGlobalNewsPost (models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=20)
    globalslug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="Index/images", default="")
    created_on = models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' ---  by ---  ' + self.author


class IndexPrivateJobPost (models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=20)
    privateslug = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="Index/images", default="")
    created_on = models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + ' ---   by  ---  ' + self.author

