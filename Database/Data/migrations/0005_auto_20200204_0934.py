# Generated by Django 2.2.1 on 2020-02-04 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0004_auto_20200204_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='classroom',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Data.Classroom'),
        ),
        migrations.AlterField(
            model_name='child',
            name='school',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Data.School'),
        ),
        migrations.AlterField(
            model_name='child',
            name='teacher',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Data.Teacher'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='current_task',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Data.Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='teacher',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Data.Teacher'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='classroom',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Data.Classroom'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Data.School'),
        ),
    ]