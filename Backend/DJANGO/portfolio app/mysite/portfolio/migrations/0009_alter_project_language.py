# Generated by Django 4.2.4 on 2023-08-21 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_project_itchurl_alter_project_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.CharField(blank=True, choices=[('C', 'C/C++'), ('UNITY', 'UNITY'), ('PYTHON', 'PYTHON'), ('JAVA', 'JAVA'), ('JAVASCRIPT', 'JAVASCRIPT')], default='C', help_text='Programming Language used in the project', max_length=10),
        ),
    ]
