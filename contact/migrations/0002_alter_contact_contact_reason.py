# Generated by Django 3.2.3 on 2021-06-21 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_reason',
            field=models.CharField(choices=[('general_query', 'General Query'), ('technical_issue', 'Technical Issue'), ('delivery', 'Delivery'), ('collection', 'Collection')], default='general_query', max_length=50),
        ),
    ]