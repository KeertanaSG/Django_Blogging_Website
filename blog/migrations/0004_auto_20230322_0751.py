# Generated by Django 2.1 on 2023-03-22 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230322_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='unassigned', max_length=255),
        ),
    ]