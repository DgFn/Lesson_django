# Generated by Django 4.2.13 on 2024-07-11 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('likes', '0002_likecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likecomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_comment', to='comments.comment'),
        ),
    ]