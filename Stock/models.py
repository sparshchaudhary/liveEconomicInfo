from django.db import models

# Create your models here.

class SwingTradePost (models.Model):
    sno = models.AutoField(primary_key=True)
    date = models.CharField(max_length=150)
    stockname = models.CharField(max_length=150)
    sector = models.CharField(max_length=150)
    priceandaction = models.CharField(max_length=150)
    content = models.TextField()
    slug = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.stockname + ' ---- SWING TRADE -- POSTED ON  ----  ' + self.date

class PreviousSwingTrade (models.Model):
    sno = models.AutoField(primary_key=True)
    date = models.CharField(max_length=150)
    stockname = models.CharField(max_length=150)
    priceandaction = models.CharField(max_length=150)
    time = models.CharField(max_length=150)
    status = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.stockname + ' ---- PREVIOUS SWING TRADE -- POSTED ON  ----  ' + self.date

class StockCard (models.Model):
    sno = models.AutoField(primary_key=True)
    cardheading = models.CharField(max_length=150)
    stockname1 = models.CharField(max_length=150)
    stockname2 = models.CharField(max_length=150)
    stockname3 = models.CharField(max_length=150)
    stockname4 = models.CharField(max_length=150)
    stockname5 = models.CharField(max_length=150)
    id = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.cardheading

class LongTermBet (models.Model):
    sno = models.AutoField(primary_key=True)
    date = models.CharField(max_length=150)
    stockname = models.CharField(max_length=150)
    intrinscivalue = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)
    timeStamp = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.stockname + ' ---- Long Term Trade -- POSTED ON  ----  ' + self.date




