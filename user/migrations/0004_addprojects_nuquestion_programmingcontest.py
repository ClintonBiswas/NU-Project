# Generated by Django 4.2.1 on 2023-05-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_name_refbooks_book_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('bio', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='project_image')),
            ],
        ),
        migrations.CreateModel(
            name='NuQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('question_year', models.IntegerField()),
                ('question_type', models.CharField(choices=[('Mid Question', 'Mid Question'), ('Mid Question', 'Mid Question')], max_length=100)),
                ('question_image', models.ImageField(upload_to='question_image')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingContest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_name', models.CharField(max_length=200)),
                ('organization_name', models.CharField(blank=True, max_length=200, null=True)),
                ('schedule', models.TextField()),
                ('join_link', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
