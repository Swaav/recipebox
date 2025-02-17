# Generated by Django 2.2.7 on 2019-12-05 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='D_favorite', to='recipebox.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='D_author', to='recipebox.Author'),
        ),
    ]
