# Generated by Django 4.2.6 on 2023-12-19 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0002_externalarticle_rename_description_article_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='ExternalArticle',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='text',
            new_name='content',
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='dislikes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='newsApp.article'),
        ),
    ]
