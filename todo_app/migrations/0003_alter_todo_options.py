# Generated by Django 4.0.3 on 2022-03-29 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_alter_todo_options_todo_is_complete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['created_at', 'is_complete']},
        ),
    ]
