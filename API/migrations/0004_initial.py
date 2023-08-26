# Generated by Django 4.0.2 on 2022-03-31 08:31

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('API', '0003_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('slug', models.SlugField(auto_created=True)),
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=255)),
                ('profile', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('content', tinymce.models.HTMLField()),
                ('isActive', models.BooleanField(default=False)),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
    ]
