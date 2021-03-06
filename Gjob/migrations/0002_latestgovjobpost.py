# Generated by Django 3.1.1 on 2020-11-09 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gjob', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestGovJobPost',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('Gslug', models.CharField(max_length=150)),
                ('views', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='GovernmentJob/jobpost')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
