# Generated by Django 4.2.1 on 2023-05-31 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('title', models.CharField(choices=[('LEAD', 'Team Lead'), ('MID', 'Mid Lead'), ('JUN', 'Junior')], max_length=4)),
                ('salary', models.IntegerField(default=80000)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Prefer Not To Say')], max_length=1)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='personnel_app.department')),
            ],
        ),
    ]
