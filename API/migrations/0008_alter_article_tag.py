# Generated by Django 4.0.2 on 2022-03-31 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_article_ispinned_delete_pinned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
