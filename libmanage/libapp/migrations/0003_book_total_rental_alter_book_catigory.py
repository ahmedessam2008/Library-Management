# Generated by Django 4.0.4 on 2022-05-13 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0002_book_photo_author_book_photo_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rental',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='catigory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libapp.catigory'),
        ),
    ]