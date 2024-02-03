# Generated by Django 4.2.9 on 2024-02-02 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fin', models.CharField(blank=True, max_length=255, null=True)),
                ('Sea', models.BooleanField(blank=True, default=False, null=True)),
                ('TMG', models.BooleanField(blank=True, default=False, null=True)),
                ('Efis', models.BooleanField(blank=True, default=False, null=True)),
                ('FNPT', models.IntegerField(blank=True, default=0, null=True)),
                ('Make', models.CharField(blank=True, max_length=255, null=True)),
                ('Run2', models.BooleanField(blank=True, default=False, null=True)),
                ('Class', models.IntegerField(blank=True, null=True)),
                ('Model', models.CharField(blank=True, max_length=255, null=True)),
                ('Power', models.IntegerField(blank=True, null=True)),
                ('Seats', models.IntegerField(blank=True, null=True)),
                ('Active', models.BooleanField(blank=True, null=True)),
                ('Kg5700', models.BooleanField(blank=True, null=True)),
                ('Rating', models.CharField(blank=True, max_length=50, null=True)),
                ('Company', models.CharField(blank=True, max_length=255, null=True)),
                ('Complex', models.BooleanField(blank=True, null=True)),
                ('CondLog', models.IntegerField(blank=True, null=True)),
                ('EngType', models.IntegerField(blank=True, null=True)),
                ('FavList', models.BooleanField(blank=True, null=True)),
                ('Category', models.IntegerField(blank=True, null=True)),
                ('HighPerf', models.BooleanField(blank=True, null=True)),
                ('SubModel', models.CharField(blank=True, max_length=50, null=True)),
                ('Aerobatic', models.BooleanField(blank=True, null=True)),
                ('RefSearch', models.CharField(blank=True, max_length=50, null=True)),
                ('Reference', models.CharField(blank=True, max_length=50, null=True)),
                ('Tailwheel', models.BooleanField(blank=True, null=True)),
                ('DefaultApp', models.IntegerField(blank=True, null=True)),
                ('DefaultLog', models.IntegerField(blank=True, null=True)),
                ('DefaultOps', models.IntegerField(blank=True, null=True)),
                ('DeviceCode', models.IntegerField(blank=True, null=True)),
                ('AircraftCode', models.CharField(blank=True, max_length=40, null=True)),
                ('DefaultLaunch', models.IntegerField(blank=True, null=True)),
                ('Record_Modified', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Airfield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(blank=True, max_length=125, null=True)),
                ('AFCat', models.IntegerField(blank=True, null=True)),
                ('AFFAA', models.CharField(blank=True, max_length=125, null=True)),
                ('Notes', models.TextField(blank=True, max_length=500, null=True)),
                ('AFCode', models.CharField(blank=True, max_length=40, null=True)),
                ('AFIATA', models.CharField(blank=True, max_length=125, null=True)),
                ('AFICAO', models.CharField(blank=True, max_length=50, null=True)),
                ('AFName', models.CharField(blank=True, max_length=125, null=True)),
                ('TZCode', models.IntegerField(blank=True, null=True)),
                ('Latitude', models.IntegerField(blank=True, null=True)),
                ('ShowList', models.BooleanField(blank=True, null=True)),
                ('UserEdit', models.BooleanField(blank=True, null=True)),
                ('AFCountry', models.IntegerField(blank=True, null=True)),
                ('Longitude', models.IntegerField(blank=True, null=True)),
                ('NotesUser', models.CharField(blank=True, max_length=125, null=True)),
                ('RegionUser', models.IntegerField(blank=True, null=True)),
                ('ElevationFT', models.IntegerField(blank=True, null=True)),
                ('Record_Modified', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PF', models.BooleanField(blank=True, null=True)),
                ('Pax', models.IntegerField(blank=True, null=True)),
                ('Fuel', models.IntegerField(blank=True, null=True)),
                ('Cargo', models.IntegerField(blank=True, null=True)),
                ('DeIce', models.BooleanField(blank=True, null=True)),
                ('Route', models.CharField(blank=True, max_length=50, null=True)),
                ('ToDay', models.IntegerField(blank=True, null=True)),
                ('minU1', models.IntegerField(blank=True, null=True)),
                ('minU2', models.IntegerField(blank=True, null=True)),
                ('minU3', models.IntegerField(blank=True, null=True)),
                ('minU4', models.IntegerField(blank=True, null=True)),
                ('minXC', models.IntegerField(blank=True, null=True)),
                ('ArrRwy', models.CharField(blank=True, max_length=10, null=True)),
                ('DepRwy', models.CharField(blank=True, max_length=10, null=True)),
                ('LdgDay', models.IntegerField(blank=True, null=True)),
                ('LiftSW', models.IntegerField(blank=True, null=True)),
                ('P1Code', models.CharField(blank=True, max_length=40, null=True)),
                ('P2Code', models.CharField(blank=True, max_length=40, null=True)),
                ('P3Code', models.CharField(blank=True, max_length=40, null=True)),
                ('P4Code', models.CharField(blank=True, max_length=40, null=True)),
                ('Report', models.CharField(blank=True, max_length=255, null=True)),
                ('TagOps', models.CharField(blank=True, max_length=50, null=True)),
                ('ToEdit', models.BooleanField(blank=True, null=True)),
                ('minAIR', models.IntegerField(blank=True, null=True)),
                ('minCOP', models.IntegerField(blank=True, null=True)),
                ('minIFR', models.IntegerField(blank=True, null=True)),
                ('minIMT', models.IntegerField(blank=True, null=True)),
                ('minPIC', models.IntegerField(blank=True, null=True)),
                ('minREL', models.IntegerField(blank=True, null=True)),
                ('minSFR', models.IntegerField(blank=True, null=True)),
                ('ArrCode', models.CharField(blank=True, max_length=40, null=True)),
                ('DateUTC', models.DateField(blank=True, null=True)),
                ('DepCode', models.CharField(blank=True, max_length=40, null=True)),
                ('HobbsIn', models.IntegerField(blank=True, null=True)),
                ('Holding', models.IntegerField(blank=True, null=True)),
                ('Pairing', models.CharField(blank=True, max_length=50, null=True)),
                ('Remarks', models.CharField(blank=True, max_length=50, null=True)),
                ('SignBox', models.IntegerField(blank=True, null=True)),
                ('ToNight', models.IntegerField(blank=True, null=True)),
                ('UserNum', models.IntegerField(blank=True, null=True)),
                ('minDUAL', models.IntegerField(blank=True, null=True)),
                ('minEXAM', models.IntegerField(blank=True, null=True)),
                ('CrewList', models.CharField(blank=True, max_length=50, null=True)),
                ('DateBASE', models.DateField(blank=True, null=True)),
                ('FuelUsed', models.IntegerField(blank=True, null=True)),
                ('HobbsOut', models.IntegerField(blank=True, null=True)),
                ('LdgNight', models.IntegerField(blank=True, null=True)),
                ('NextPage', models.BooleanField(blank=True, null=True)),
                ('TagDelay', models.CharField(blank=True, max_length=50, null=True)),
                ('Training', models.CharField(blank=True, max_length=50, null=True)),
                ('UserBool', models.BooleanField(blank=True, null=True)),
                ('UserText', models.CharField(blank=True, max_length=50, null=True)),
                ('minINSTR', models.IntegerField(blank=True, null=True)),
                ('minNIGHT', models.IntegerField(blank=True, null=True)),
                ('minPICUS', models.IntegerField(blank=True, null=True)),
                ('minTOTAL', models.IntegerField(blank=True, null=True)),
                ('ArrOffset', models.IntegerField(blank=True, null=True)),
                ('DateLOCAL', models.DateField(blank=True, null=True)),
                ('DepOffset', models.IntegerField(blank=True, null=True)),
                ('TagLaunch', models.CharField(blank=True, max_length=50, null=True)),
                ('TagLesson', models.CharField(blank=True, max_length=50, null=True)),
                ('ToTimeUTC', models.IntegerField(blank=True, null=True)),
                ('ArrTimeUTC', models.IntegerField(blank=True, null=True)),
                ('BaseOffset', models.IntegerField(blank=True, null=True)),
                ('DepTimeUTC', models.IntegerField(blank=True, null=True)),
                ('FlightCode', models.CharField(blank=True, max_length=40, null=True)),
                ('LdgTimeUTC', models.IntegerField(blank=True, null=True)),
                ('FuelPlanned', models.IntegerField(blank=True, null=True)),
                ('NextSummary', models.BooleanField(blank=True, null=True)),
                ('TagApproach', models.CharField(blank=True, max_length=10, null=True)),
                ('AircraftCode', models.CharField(blank=True, max_length=40, null=True)),
                ('ArrTimeSCHED', models.IntegerField(blank=True, null=True)),
                ('DepTimeSCHED', models.IntegerField(blank=True, null=True)),
                ('FlightNumber', models.CharField(blank=True, max_length=10, null=True)),
                ('FlightSearch', models.CharField(blank=True, max_length=40, null=True)),
                ('Record_Modified', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imagepic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FileExt', models.CharField(blank=True, max_length=10, null=True)),
                ('ImgCode', models.CharField(blank=True, max_length=40, null=True)),
                ('FileName', models.CharField(blank=True, max_length=40, null=True)),
                ('LinkCode', models.CharField(blank=True, max_length=40, null=True)),
                ('Img_Upload', models.BooleanField(blank=True, null=True)),
                ('Img_Download', models.BooleanField(blank=True, null=True)),
                ('Record_Modified', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='LimitRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LTo', models.CharField(blank=True, max_length=16, null=True)),
                ('LFrom', models.CharField(blank=True, max_length=16, null=True)),
                ('LType', models.IntegerField(blank=True, null=True)),
                ('LZone', models.IntegerField(blank=True, null=True)),
                ('LMinutes', models.IntegerField(blank=True, null=True)),
                ('LimitCode', models.CharField(blank=True, max_length=60, null=True)),
                ('LPeriodCode', models.IntegerField(blank=True, null=True)),
                ('Record_Modified', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Limit rule',
                'verbose_name_plural': 'Limit rules',
            },
        ),
        migrations.CreateModel(
            name='MyQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
                ('mQCode', models.CharField(blank=True, max_length=255, null=True)),
                ('QuickView', models.BooleanField(blank=True, null=True)),
                ('ShortName', models.CharField(blank=True, max_length=255, null=True)),
                ('Record_Modified', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Query',
                'verbose_name_plural': 'Queries',
            },
        ),
        migrations.CreateModel(
            name='MyQueryBuild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Build1', models.CharField(blank=True, max_length=60, null=True)),
                ('Build2', models.IntegerField(blank=True, null=True)),
                ('Build3', models.IntegerField(blank=True, null=True)),
                ('Build4', models.CharField(blank=True, max_length=60, null=True)),
                ('mQCode', models.CharField(blank=True, max_length=60, null=True)),
                ('mQBCode', models.CharField(blank=True, max_length=60, null=True)),
                ('Record_Modified', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Build',
                'verbose_name_plural': 'Builds',
            },
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notes', models.TextField(blank=True, max_length=500, null=True)),
                ('Active', models.BooleanField(blank=True, null=True)),
                ('Company', models.CharField(blank=True, max_length=50, null=True)),
                ('FavList', models.BooleanField(blank=True, null=True)),
                ('UserAPI', models.CharField(blank=True, max_length=125, null=True)),
                ('Facebook', models.CharField(blank=True, max_length=125, null=True)),
                ('LinkedIn', models.CharField(blank=True, max_length=125, null=True)),
                ('PilotRef', models.CharField(blank=True, max_length=125, null=True)),
                ('PilotCode', models.CharField(blank=True, max_length=60, null=True)),
                ('PilotName', models.CharField(blank=True, max_length=50, null=True)),
                ('PilotEMail', models.CharField(blank=True, max_length=125, null=True)),
                ('PilotPhone', models.CharField(blank=True, max_length=50, null=True)),
                ('Certificate', models.CharField(blank=True, max_length=50, null=True)),
                ('PhoneSearch', models.CharField(blank=True, max_length=125, null=True)),
                ('PilotSearch', models.CharField(blank=True, max_length=125, null=True)),
                ('RosterAlias', models.CharField(blank=True, max_length=125, null=True)),
                ('Record_Modified', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PolitlogHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('table', models.CharField(blank=True, max_length=255, null=True)),
                ('guid', models.CharField(blank=True, max_length=255, null=True)),
                ('platform', models.IntegerField(blank=True, null=True)),
                ('modified', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QCode', models.CharField(blank=True, max_length=125, null=True)),
                ('RefExtra', models.IntegerField(blank=True, null=True)),
                ('RefModel', models.CharField(blank=True, max_length=10, null=True)),
                ('Validity', models.IntegerField(blank=True, null=True)),
                ('DateValid', models.CharField(blank=True, max_length=10, null=True)),
                ('QTypeCode', models.IntegerField(blank=True, null=True)),
                ('DateIssued', models.CharField(blank=True, max_length=10, null=True)),
                ('MinimumQty', models.IntegerField(blank=True, null=True)),
                ('NotifyDays', models.IntegerField(blank=True, null=True)),
                ('RefAirfield', models.CharField(blank=True, max_length=125, null=True)),
                ('MinimumPeriod', models.IntegerField(blank=True, null=True)),
                ('NotifyComment', models.CharField(blank=True, max_length=125, null=True)),
                ('Record_Modified', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SettingConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.CharField(blank=True, max_length=50, null=True)),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Group', models.CharField(blank=True, max_length=50, null=True)),
                ('ConfigCode', models.IntegerField(blank=True, null=True)),
                ('Record_Modified', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Config',
                'verbose_name_plural': 'Configs',
            },
        ),
    ]