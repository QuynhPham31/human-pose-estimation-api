# Generated by Django 2.0.2 on 2018-03-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180328_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinput',
            name='body_waist',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='userinput',
            name='bust_waist',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='userinput',
            name='legs_body',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='userinput',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='userinput',
            name='shoulder_hips',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='userinput',
            name='waist_hips',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
