# Generated by Django 2.2.2 on 2020-08-18 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='class_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Class', verbose_name='所在班级'),
        ),
    ]