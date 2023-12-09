# Generated by Django 5.0 on 2023-12-09 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги статей'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='article',
            field=models.ManyToManyField(related_name='tag', through='articles.Scope', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Название'),
        ),
    ]