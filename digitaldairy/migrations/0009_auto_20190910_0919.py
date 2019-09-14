# Generated by Django 2.2 on 2019-09-10 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digitaldairy', '0008_auto_20190831_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeSalaries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('salary_paid_date', models.DateField()),
                ('salary_date', models.DateField(null=True)),
                ('salary_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('employee', models.ForeignKey(db_column='employee', on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.Employees')),
            ],
            options={
                'db_table': 'employee_salaries',
            },
        ),
        migrations.CreateModel(
            name='SalaryAdvances',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('advance_date', models.DateField(null=True)),
                ('salary_date', models.DateField(null=True)),
                ('advance_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('employee', models.ForeignKey(db_column='employee', on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.Employees')),
            ],
            options={
                'db_table': 'employees_salary_advances',
            },
        ),
        migrations.DeleteModel(
            name='salaries_and_advances',
        ),
    ]