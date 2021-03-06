# Generated by Django 3.1.1 on 2020-11-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0003_stockmarketopinion'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockMarketOpinionPost',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('stockopinionslug', models.CharField(max_length=150)),
                ('views', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='StockMarket/Opinion')),
                ('sector', models.CharField(max_length=150)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.DeleteModel(
            name='StockMarketOpinion',
        ),
    ]
