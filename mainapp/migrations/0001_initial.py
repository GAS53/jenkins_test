# Generated by Django 4.2.5 on 2023-09-15 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('email', models.CharField(default='', max_length=40, unique=True, verbose_name='email')),
                ('last_name', models.CharField(default='', max_length=40, verbose_name='фамилия')),
                ('first_name', models.CharField(default='', max_length=40, verbose_name='имя')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='есть ли доступ к системе')),
                ('is_active', models.BooleanField(default=True, verbose_name='активен ли сейчас пользователь')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='администратор всей системы')),
                ('is_manager', models.BooleanField(default=False, verbose_name='менеджер')),
                ('is_constructor', models.BooleanField(default=False, verbose_name='проектировщик')),
                ('is_checker', models.BooleanField(default=False, verbose_name='проверяющий')),
                ('is_teh_control', models.BooleanField(default=False, verbose_name='нормоконтроль')),
                ('is_approver', models.BooleanField(default=False, verbose_name='утверждающий')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
        ),
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('id', models.PositiveBigIntegerField(auto_created=True, db_index=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Запись удалена')),
                ('description', models.CharField(default='', max_length=36, verbose_name='описание проекта')),
            ],
            options={
                'verbose_name': 'сборка',
                'verbose_name_plural': 'сборки',
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.PositiveBigIntegerField(auto_created=True, db_index=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Запись удалена')),
                ('name', models.CharField(default='', max_length=50, verbose_name='название детали')),
                ('assembly', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='detail', to='mainapp.assembly', verbose_name='сборка')),
            ],
            options={
                'verbose_name': 'деталь',
                'verbose_name_plural': 'детали',
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.PositiveBigIntegerField(auto_created=True, db_index=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Запись удалена')),
                ('name', models.CharField(default='', max_length=36, verbose_name='название')),
                ('description', models.CharField(default='', max_length=50, verbose_name='описание')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='stage_creator', to=settings.AUTH_USER_MODEL, verbose_name='создатель стадии')),
                ('responsible_worker', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='stage_worker', to=settings.AUTH_USER_MODEL, verbose_name='исполнитель стадии')),
            ],
            options={
                'verbose_name': 'стадия',
                'verbose_name_plural': 'стадии',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.PositiveBigIntegerField(auto_created=True, db_index=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('description', models.CharField(default='', max_length=50, verbose_name='описание проекта')),
                ('is_deleted', models.BooleanField(verbose_name='проект удален')),
                ('is_immutable', models.BooleanField(verbose_name='неизменяемый(после сдачи в архив)')),
                ('now_stage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='stage', to='mainapp.stage')),
            ],
            options={
                'verbose_name': 'проект',
                'verbose_name_plural': 'проекты',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.PositiveBigIntegerField(auto_created=True, db_index=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Запись удалена')),
                ('name', models.CharField(default='', max_length=36, verbose_name='название материала')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='material', to='mainapp.detail', verbose_name='материал')),
            ],
            options={
                'verbose_name': 'материал',
                'verbose_name_plural': 'материалы',
            },
        ),
        migrations.AddField(
            model_name='assembly',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.project'),
        ),
    ]