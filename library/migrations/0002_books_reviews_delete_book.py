# Generated by Django 5.1.4 on 2025-01-12 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Укажите название книги:')),
                ('description', models.TextField(blank=True, verbose_name='Укажите описание книги:')),
                ('price', models.PositiveIntegerField(default=20, verbose_name='Укажите цену книги:')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода:')),
                ('genre', models.CharField(choices=[('Фантастика', 'Фантастика'), ('Новелла', 'Новелла'), ('Ужасы', 'Ужасы')], max_length=100, verbose_name='Укажите жанр книги:')),
                ('author_email', models.EmailField(blank=True, max_length=254, verbose_name='Укажите почту автора:')),
                ('author_name', models.TextField(verbose_name='Укажите имя автора:')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'список книг',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(verbose_name='Напишите комментарий к книге:')),
                ('stars', models.CharField(choices=[('🌟', '🌟'), ('🌟🌟', '🌟🌟'), ('🌟🌟🌟', '🌟🌟🌟'), ('🌟🌟🌟🌟', '🌟🌟🌟🌟'), ('🌟🌟🌟🌟🌟🌟', '🌟🌟🌟🌟🌟')], default='🌟🌟🌟🌟🌟🌟', max_length=100)),
                ('GENRE_CHOICES', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='library.books')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
