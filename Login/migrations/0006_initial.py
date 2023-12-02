# Generated by Django 4.2.6 on 2023-10-06 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Login', '0005_delete_emprendimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_prod', models.CharField(max_length=50)),
                ('descripcion_prod', models.CharField(max_length=150)),
                ('imagen_prod', models.ImageField(null=True, upload_to='images')),
                ('activo', models.CharField(max_length=1)),
                ('precio', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]