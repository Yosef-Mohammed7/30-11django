# Generated by Django 3.0.9 on 2020-11-25 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
        ('courses', '0004_auto_20201125_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('allowed_memberships', models.ManyToManyField(to='memberships.Membership')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=120)),
                ('position', models.IntegerField()),
                ('video_url', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.Course')),
            ],
        ),
        migrations.DeleteModel(
            name='classes',
        ),
    ]
