# Generated by Django 2.1.7 on 2019-06-15 21:12

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30, null=True)),
                ('owner', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_name', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('price', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Common',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=250)),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test1.City')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persent', models.IntegerField(null=True)),
                ('expire_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pre_Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger', models.CharField(max_length=100, null=True)),
                ('driver', models.CharField(max_length=100, null=True)),
                ('cost', models.FloatField(null=True)),
                ('date', models.DateField(null=True)),
                ('payment_status', models.CharField(choices=[('CASH', 'cash'), ('ONLINE', 'online')], max_length=6)),
                ('distance', models.FloatField(null=True)),
                ('total_stop', models.FloatField(null=True)),
                ('accepted', models.BooleanField(default=False)),
                ('end', models.BooleanField(default=False)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test1.City')),
                ('drop', models.ManyToManyField(related_name='drop_point', to='test1.Location')),
                ('pickup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pickup_point', to='test1.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('string', models.CharField(max_length=300, null=True)),
                ('user', models.CharField(max_length=100, null=True)),
                ('pre_vote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test1.Pre_Vote')),
                ('travel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test1.Travel')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('balance', models.IntegerField(default=0)),
                ('permission', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('balance', models.FloatField(default=0.0)),
                ('offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test1.Offer')),
            ],
        ),
        migrations.AddField(
            model_name='common',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test1.Location'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test1.City'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('place_name', 'id')},
        ),
    ]
