# Generated by Django 4.0.2 on 2022-03-31 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_gallery_newsletter_videos_alter_article_profile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='isPinned',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Pinned',
        ),
    ]
