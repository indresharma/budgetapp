# Generated by Django 3.0.3 on 2020-02-21 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expensemanager', '0003_auto_20200221_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Trans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('trans_choice', models.CharField(choices=[('Income', 'Income'), ('Expense', 'Expense')], max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('amount', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expensemanager.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='category',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
