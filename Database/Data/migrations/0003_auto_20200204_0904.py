# Generated by Django 2.2.1 on 2020-02-04 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0002_auto_20200204_0841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='Classroom',
            new_name='classroom',
        ),
        migrations.RenameField(
            model_name='child',
            old_name='School',
            new_name='school',
        ),
        migrations.RenameField(
            model_name='child',
            old_name='Teacher',
            new_name='teacher',
        ),
        migrations.AddField(
            model_name='classroom',
            name='current_task',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Data.Task'),
        ),
        migrations.AddField(
            model_name='task',
            name='teacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Data.Teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='classroom',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Data.Classroom'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Data.School'),
        ),
        migrations.AlterField(
            model_name='child',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
