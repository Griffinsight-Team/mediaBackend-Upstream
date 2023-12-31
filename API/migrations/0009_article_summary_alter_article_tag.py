# Generated by Django 4.0.2 on 2022-04-01 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_alter_article_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(blank=True, choices=[('Academic', 'Academic'), ('Campus', 'Campus'), ('Spotlight', 'Spotlight'), ('Sports', 'Sports')], max_length=100, null=True),
        ),
    ]
