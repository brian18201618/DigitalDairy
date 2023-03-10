# Generated by Django 2.2 on 2019-08-15 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AiRecords',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('service_date', models.DateField(db_index=True)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('vet_name', models.CharField(blank=True, default='', max_length=100)),
                ('open_days', models.IntegerField(default=0, null=True)),
                ('repeats', models.IntegerField(default=0, null=True)),
                ('inbreeding', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=5)),
                ('first_heat_check_date', models.DateField(null=True)),
                ('second_heat_check_date', models.DateField(null=True)),
                ('drying_date', models.DateField(null=True)),
                ('steaming_date', models.DateField(null=True)),
                ('pregnancy_check_date', models.DateField(null=True)),
                ('pregnancy_diagnosis_date', models.DateField(null=True)),
                ('pregnancy_diagnosis_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('pregnancy_diagnosis_vet_name', models.CharField(blank=True, default='', max_length=100)),
                ('pregnancy_diagnosis_result', models.CharField(choices=[('Positive', 'Positive'), ('Negative', 'Negative'), ('Unconfirmed', 'Unconfirmed'), ('Failed', 'Failed')], default='Unconfirmed', max_length=20)),
                ('calving_status', models.CharField(choices=[('Not Yet', 'Not Yet'), ('Calved', 'Calved'), ('Miscarriaged', 'Miscarriaged'), ('Aborted', 'Aborted')], default='Not Yet', max_length=100)),
                ('due_date', models.DateField(null=True)),
            ],
            options={
                'db_table': 'ai_records',
                'ordering': ['-service_date'],
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, default='', max_length=100)),
                ('contacts', models.CharField(blank=True, default='', max_length=30)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='Consumers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, default='', max_length=100)),
                ('contacts', models.CharField(blank=True, default='', max_length=30)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'consumers',
            },
        ),
        migrations.CreateModel(
            name='Cow',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('lactations', models.IntegerField(default=0, null=True)),
                ('grade', models.CharField(blank=True, choices=[('PEDIGREE', 'PEDIGREE'), ('APPENDIX', 'APPENDIX'), ('POOL', 'POOL'), ('INTERMEDIATE', 'INTERMEDIATE'), ('FOUNDATION', 'FOUNDATION')], default='PEDIGREE', max_length=30)),
                ('breed', models.CharField(blank=True, default='', max_length=30)),
                ('color', models.CharField(blank=True, default='', max_length=30)),
                ('dob', models.DateField()),
                ('group', models.CharField(blank=True, default='', max_length=30)),
                ('status', models.CharField(blank=True, default='Open', max_length=30)),
                ('birth_weight', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('category', models.CharField(choices=[('Milker', 'Milker'), ('Heifer', 'Heifer'), ('Dry', 'Dry'), ('Steamer', 'Steamer'), ('Incalf Heifer', 'Incalf Heifer'), ('Calf', 'Calf'), ('Weaner', 'Weaner'), ('Weaner 1', 'Weaner 1'), ('Weaner 2', 'Weaner 2'), ('Weaner 3', 'Weaner 3'), ('Yearling', 'Yearling'), ('Bulling', 'Bulling'), ('Bull', 'Bull')], default='Heifer', max_length=30)),
                ('source', models.CharField(blank=True, default='', max_length=50)),
                ('dam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cow_dam', to='digitaldairy.Cow')),
            ],
            options={
                'db_table': 'cow',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_discovered', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(blank=True, default='', max_length=1000)),
            ],
            options={
                'db_table': 'disease_records',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('date_hired', models.DateField(null=True)),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(blank=True, default='', max_length=100)),
                ('designation', models.CharField(blank=True, default='', max_length=100)),
                ('contacts', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('source', models.CharField(blank=True, default='', max_length=30)),
            ],
            options={
                'db_table': 'expense',
            },
        ),
        migrations.CreateModel(
            name='FeedFormulation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=30, unique=True)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'feed_formulation',
            },
        ),
        migrations.CreateModel(
            name='FeedItems',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('unit_of_measure', models.CharField(blank=True, default='', max_length=30)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('initial_stock', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('available_stock', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('reorder_level', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'feed_item',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('source', models.CharField(blank=True, default='', max_length=30)),
            ],
            options={
                'db_table': 'income',
            },
        ),
        migrations.CreateModel(
            name='SemenRecords',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bull_code', models.CharField(max_length=100)),
                ('bull_name', models.CharField(blank=True, max_length=100)),
                ('bull_breed', models.CharField(blank=True, default='', max_length=100)),
                ('num_of_straws', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cost_per_straw', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('company_name', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'db_table': 'semen_records',
            },
        ),
        migrations.CreateModel(
            name='AbortionMiscarriages',
            fields=[
                ('ai_record', models.ForeignKey(db_column='ai_record', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='digitaldairy.AiRecords')),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('Miscarriage', 'Miscarriage'), ('Abortion', 'Abortion')], max_length=20)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('cause', models.CharField(blank=True, default='', max_length=1000)),
                ('vet_name', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'db_table': 'abortion_miscarriages',
            },
        ),
        migrations.CreateModel(
            name='CowBodyTraits',
            fields=[
                ('cow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='digitaldairy.Cow')),
                ('frame', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('dairy_strength', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('udder', models.CharField(blank=True, default='', max_length=10)),
                ('feet_legs', models.CharField(blank=True, default='', max_length=10)),
                ('stature', models.CharField(blank=True, default='', max_length=10)),
                ('chest_width', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('body_depth', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('angularity', models.CharField(blank=True, default='', max_length=10)),
                ('cond_score', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('thurl_width', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('rump_angle', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('rump_width', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('right_legs_rv', models.CharField(blank=True, default='', max_length=10)),
                ('right_legs_sv', models.CharField(blank=True, default='', max_length=10)),
                ('foot_angle', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('locomotion', models.CharField(blank=True, default='', max_length=10)),
            ],
            options={
                'db_table': 'cow_body_traits',
            },
        ),
        migrations.CreateModel(
            name='CowSales',
            fields=[
                ('cow', models.ForeignKey(db_column='cow', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='digitaldairy.Cow')),
                ('client_name', models.CharField(blank=True, default='', max_length=100)),
                ('date', models.DateField(db_column='date')),
                ('cow_value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('sale_remarks', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'db_table': 'cow_sales',
            },
        ),
        migrations.CreateModel(
            name='Deaths',
            fields=[
                ('cow', models.ForeignKey(db_column='cow', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='digitaldairy.Cow')),
                ('death_date', models.DateField(null=True)),
                ('death_cause', models.CharField(blank=True, default='', max_length=100)),
                ('autopsy_date', models.DateField(null=True)),
                ('autopsy_results', models.CharField(blank=True, default='', max_length=255)),
                ('autopsy_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('vet_name', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'db_table': 'death_records',
            },
        ),
        migrations.CreateModel(
            name='MilkTargets',
            fields=[
                ('cow_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='digitaldairy.Cow', unique=True)),
                ('target_quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'db_table': 'milk_targets',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
                ('client_address', models.CharField(blank=True, default='', max_length=100)),
                ('farm_name', models.CharField(blank=True, default='', max_length=100)),
                ('farm_location', models.CharField(blank=True, default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentRecords',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('diagnosis', models.CharField(blank=True, default='', max_length=100)),
                ('disease', models.CharField(blank=True, default='', max_length=100)),
                ('date', models.DateField(db_index=True)),
                ('treatment_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('treatment', models.CharField(blank=True, default='', max_length=100)),
                ('vet_name', models.CharField(blank=True, default='', max_length=100)),
                ('cow', models.ForeignKey(db_column='cow', on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.Cow')),
            ],
            options={
                'db_table': 'treatment_records',
            },
        ),
        migrations.CreateModel(
            name='salaries_and_advances',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('advance_date', models.DateField(null=True)),
                ('salary_date', models.DateField(null=True)),
                ('ending_month_date', models.DateField(null=True)),
                ('advance_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('salary_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('balance_after_salary', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('balance_after_advance', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('employee', models.ForeignKey(db_column='employee', on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.Employees')),
            ],
            options={
                'db_table': 'salaries_advances',
            },
        ),
        migrations.CreateModel(
            name='MilkSalesPayments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True)),
                ('date_of_payment', models.DateField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.Clients')),
            ],
            options={
                'db_table': 'milk_sales_payments',
            },
        ),
        migrations.CreateModel(
            name='FeedingProgramme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('feeding_category', models.CharField(choices=[('Milker', 'Milker'), ('Heifer', 'Heifer'), ('Dry', 'Dry'), ('Steamer', 'Steamer'), ('Incalf Heifer', 'Incalf Heifer'), ('Calf', 'Calf'), ('Weaner', 'Weaner'), ('Weaner 1', 'Weaner 1'), ('Weaner 2', 'Weaner 2'), ('Weaner 3', 'Weaner 3'), ('Yearling', 'Yearling'), ('Bulling', 'Bulling'), ('Bull', 'Bull')], default='Heifer', max_length=30)),
                ('feed_formulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.FeedFormulation')),
            ],
            options={
                'db_table': 'feeding_programme',
            },
        ),
        migrations.CreateModel(
            name='DailyFeeding',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('feeding_category', models.CharField(choices=[('Milker', 'Milker'), ('Heifer', 'Heifer'), ('Dry', 'Dry'), ('Steamer', 'Steamer'), ('Incalf Heifer', 'Incalf Heifer'), ('Calf', 'Calf'), ('Weaner', 'Weaner'), ('Weaner 1', 'Weaner 1'), ('Weaner 2', 'Weaner 2'), ('Weaner 3', 'Weaner 3'), ('Yearling', 'Yearling'), ('Bulling', 'Bulling'), ('Bull', 'Bull')], default='Heifer', max_length=30)),
                ('feed_formulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.FeedFormulation')),
            ],
            options={
                'db_table': 'daily_feeding',
            },
        ),
        migrations.CreateModel(
            name='CowInsurance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('policy', models.CharField(blank=True, default='', max_length=30)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('insured_value', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('premium_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('cow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.Cow')),
            ],
            options={
                'db_table': 'cow_insurance',
            },
        ),
        migrations.AddField(
            model_name='cow',
            name='sire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cow_sire', to='digitaldairy.SemenRecords'),
        ),
        migrations.CreateModel(
            name='CalfFeeding',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('milk_quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('feeding_date', models.DateField()),
                ('cow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.Cow')),
            ],
            options={
                'db_table': 'calf_feeding',
            },
        ),
        migrations.AddField(
            model_name='airecords',
            name='cow',
            field=models.ForeignKey(db_column='cow', on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.Cow'),
        ),
        migrations.AddField(
            model_name='airecords',
            name='semen_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.SemenRecords'),
        ),
        migrations.CreateModel(
            name='WeightRecords',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('weight_date', models.DateField(db_column='weight_date', db_index=True)),
                ('weight', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('height', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('cow', models.ForeignKey(db_column='cow', on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.Cow')),
            ],
            options={
                'db_table': 'weight_records',
                'ordering': ['cow', '-weight_date'],
                'unique_together': {('cow', 'weight_date')},
                'index_together': {('weight_date', 'cow')},
            },
        ),
        migrations.CreateModel(
            name='Vaccinations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vaccine', models.CharField(blank=True, default='', max_length=100)),
                ('vaccination_date', models.DateField(db_column='date', db_index=True)),
                ('next_vaccination_date', models.DateField(null=True)),
                ('vaccination_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cow', models.ForeignKey(db_column='cow', on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.Cow')),
            ],
            options={
                'db_table': 'vaccinations_records',
                'index_together': {('vaccination_date', 'cow')},
            },
        ),
        migrations.CreateModel(
            name='MilkProductions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('milk_date', models.DateField(db_column='milk_date', db_index=True)),
                ('am_quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('noon_quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('pm_quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('cow_id', models.ForeignKey(db_column='cow_id', on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.Cow')),
            ],
            options={
                'db_table': 'milk_production',
                'unique_together': {('milk_date', 'cow_id')},
                'index_together': {('milk_date', 'cow_id')},
            },
        ),
        migrations.CreateModel(
            name='MilkConsumptions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(db_column='date', db_index=True)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.Consumers')),
            ],
            options={
                'db_table': 'milk_consumption',
                'unique_together': {('date', 'consumer')},
                'index_together': {('date', 'consumer')},
            },
        ),
        migrations.CreateModel(
            name='FeedFormulationPart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('feed_formulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.FeedFormulation')),
                ('feed_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.FeedItems')),
            ],
            options={
                'db_table': 'feed_formulation_part',
                'unique_together': {('feed_item', 'feed_formulation')},
                'index_together': {('feed_item', 'feed_formulation')},
            },
        ),
        migrations.CreateModel(
            name='Deworming',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dewormer', models.CharField(blank=True, default='', max_length=100)),
                ('deworming_date', models.DateField(db_column='date', db_index=True)),
                ('next_deworming_date', models.DateField(null=True)),
                ('deworming_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cow', models.ForeignKey(db_column='cow', on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.Cow')),
            ],
            options={
                'db_table': 'deworming_records',
                'unique_together': {('deworming_date', 'cow')},
                'index_together': {('deworming_date', 'cow')},
            },
        ),
        migrations.CreateModel(
            name='Calvings',
            fields=[
                ('ai_record', models.ForeignKey(db_column='ai_record', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='digitaldairy.AiRecords')),
                ('calving_date', models.DateField()),
                ('calving_type', models.CharField(choices=[('Single', 'Single'), ('Twin', 'Twin')], default='Single', max_length=7)),
                ('calf', models.ForeignKey(db_column='calf', on_delete=django.db.models.deletion.CASCADE, to='digitaldairy.Cow')),
            ],
            options={
                'db_table': 'calving_records',
            },
        ),
        migrations.AlterUniqueTogether(
            name='airecords',
            unique_together={('service_date', 'cow')},
        ),
        migrations.AlterIndexTogether(
            name='airecords',
            index_together={('service_date', 'cow')},
        ),
    ]
