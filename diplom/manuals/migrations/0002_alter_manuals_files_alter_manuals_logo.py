# Generated by Django 5.1 on 2024-08-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manuals',
            name='files',
            field=models.FileField(blank=True, default='default.jpg', upload_to='manuals/<django.db.models.fields.related.ForeignKey>/<django.db.models.fields.CharField>/'),
        ),
        migrations.AlterField(
            model_name='manuals',
            name='logo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='manuals/<django.db.models.fields.related.ForeignKey>/<django.db.models.fields.CharField>/'),
        ),
    ]
