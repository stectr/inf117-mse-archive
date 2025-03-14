# Generated by Django 4.2.7 on 2023-11-13 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_data', '0002_rename_facultyids_facultyid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('employment_id', models.AutoField(primary_key=True, serialize=False)),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('position_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('employment_id', models.AutoField(primary_key=True, serialize=False)),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('position_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='DiversityAcitivites',
            fields=[
                ('employment_id', models.AutoField(primary_key=True, serialize=False)),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('position_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='DiversityService',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateField(verbose_name='Start Date')),
                ('enddate', models.DateField(verbose_name='End Date')),
                ('dateinput', models.CharField(blank=True, max_length=30, verbose_name='Custom Date Input')),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Diversity Activity Related to Professional and Public Service',
                'verbose_name_plural': 'Diversity Activities Related to Professional and Public Service',
            },
        ),
        migrations.CreateModel(
            name='DiversityTeaching',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateField(verbose_name='Start Date')),
                ('enddate', models.DateField(verbose_name='End Date')),
                ('dateinput', models.CharField(blank=True, max_length=30, verbose_name='Custom Date Input')),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Diversity Activity Related to Teaching',
                'verbose_name_plural': 'Diversity Activities Related to Teaching',
            },
        ),
        migrations.CreateModel(
            name='DoctoralStudent',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startyear', models.IntegerField(verbose_name='Start Year')),
                ('endyear', models.IntegerField(verbose_name='End Year')),
                ('endpresent', models.BooleanField(verbose_name='Until Present?')),
                ('studentName', models.CharField(max_length=100, verbose_name='Student Name')),
                ('role', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('comments', models.CharField(blank=True, max_length=500)),
                ('receivedPHD', models.BooleanField(verbose_name='Has this student received their Ph.D or Pharm.D?')),
                ('candidacy', models.BooleanField(verbose_name='Has this student advanced to candidacy?')),
                ('preDissComm', models.BooleanField(verbose_name='Was this student in a pre-dissertation committee?')),
                ('otherResearch', models.BooleanField(verbose_name='Other')),
            ],
            options={
                'verbose_name': 'Doctoral Student',
            },
        ),
        migrations.CreateModel(
            name='EmploymentHistory',
            fields=[
                ('employment_id', models.AutoField(primary_key=True, serialize=False)),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('title_rank', models.CharField(max_length=100)),
                ('step', models.CharField(blank=True, max_length=100, null=True)),
                ('time_percentage', models.DecimalField(decimal_places=0, max_digits=3)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HonorsAward',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateField(verbose_name='Start Date')),
                ('enddate', models.DateField(verbose_name='End Date')),
                ('dateinput', models.CharField(blank=True, max_length=30, verbose_name='Custom Date Input')),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Honors and Awards',
                'verbose_name_plural': 'Honors and Awards',
            },
        ),
        migrations.CreateModel(
            name='MasterStudent',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startyear', models.IntegerField(verbose_name='Start Year')),
                ('endyear', models.IntegerField(verbose_name='End Year')),
                ('endpresent', models.BooleanField(verbose_name='Until Present?')),
                ('studentName', models.CharField(max_length=100, verbose_name='Student Name')),
                ('role', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('comments', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'verbose_name': "Master's Student",
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateField(verbose_name='Start Date')),
                ('enddate', models.DateField(verbose_name='End Date')),
                ('endpresent', models.BooleanField(verbose_name='Until Present?')),
                ('dateinput', models.CharField(blank=True, max_length=30, verbose_name='Custom Date Input')),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Membership',
            },
        ),
        migrations.CreateModel(
            name='OtherEmployment',
            fields=[
                ('employment_id', models.AutoField(primary_key=True, serialize=False)),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('position_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='OtherResearch',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startyear', models.IntegerField(verbose_name='Start Year')),
                ('endyear', models.IntegerField(verbose_name='End Year')),
                ('endpresent', models.BooleanField(verbose_name='Until Present?')),
                ('studentName', models.CharField(max_length=100, verbose_name='Student Name')),
                ('role', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('comments', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'verbose_name': 'Other Research or Teaching Supervision',
            },
        ),
        migrations.CreateModel(
            name='PostdocStudent',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startyear', models.IntegerField(verbose_name='Start Year')),
                ('endyear', models.IntegerField(verbose_name='End Year')),
                ('endpresent', models.BooleanField(verbose_name='Until Present?')),
                ('studentName', models.CharField(max_length=100, verbose_name='Student Name')),
                ('role', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('comments', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'verbose_name': 'Postdoctoral Scholar',
            },
        ),
        migrations.CreateModel(
            name='ProfDevelopmentTeaching',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateField(verbose_name='Start Date')),
                ('enddate', models.DateField(verbose_name='End Date')),
                ('dateinput', models.CharField(blank=True, max_length=30, verbose_name='Custom Date Input')),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Professional Development Activity Related to Teaching',
                'verbose_name_plural': 'Professional Development Activities Related to Teaching',
            },
        ),
        migrations.CreateModel(
            name='ProfDevService',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateField(verbose_name='Start Date')),
                ('enddate', models.DateField(verbose_name='End Date')),
                ('dateinput', models.CharField(blank=True, max_length=30, verbose_name='Custom Date Input')),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Professional Development Activity Related to Professional and Public Service',
                'verbose_name_plural': 'Professional Development Activities Related to Professional and Public Service',
            },
        ),
        migrations.CreateModel(
            name='ProfessionalActivity',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateField(verbose_name='Start Date')),
                ('enddate', models.DateField(verbose_name='End Date')),
                ('dateinput', models.CharField(blank=True, max_length=30, verbose_name='Custom Date Input')),
                ('description', models.CharField(max_length=1000)),
                ('invitedEduGov', models.BooleanField(verbose_name='Invited presentation at an educational, governmental (or similar) institution')),
                ('invitedProf', models.BooleanField(verbose_name='Invited presentation at a professional meeting')),
                ('acceptedEduGov', models.BooleanField(verbose_name='Accepted presentation at an educational, governmental (or similar) institution')),
                ('acceptedProf', models.BooleanField(verbose_name='Accepted presentation at a professional meeting')),
                ('otherPresent', models.BooleanField(verbose_name='Other presentation at a professional meeting')),
                ('mediaInterview', models.BooleanField(verbose_name='Media Appearance and/or Interview')),
                ('articlesReviews', models.BooleanField(verbose_name='Professional article about you or published review of your work')),
            ],
            options={
                'verbose_name': 'Professional Activity',
                'verbose_name_plural': 'Professional Activities',
            },
        ),
        migrations.CreateModel(
            name='ProfessionalDevelopement',
            fields=[
                ('employment_id', models.AutoField(primary_key=True, serialize=False)),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('position_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ProfPublicService',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateField(verbose_name='Start Date')),
                ('enddate', models.DateField(verbose_name='End Date')),
                ('dateinput', models.CharField(blank=True, max_length=30, verbose_name='Custom Date Input')),
                ('description', models.CharField(max_length=1000)),
                ('profSocOutsideInst', models.BooleanField(verbose_name='Service to Professional Societies / Outside Institutions')),
                ('journalEdit', models.BooleanField(verbose_name='Journal Editor / Membership on Journal Editorial Boards')),
                ('reviewer', models.BooleanField(verbose_name='Reviewer of Manuscripts / Journal Articles')),
                ('memberReviewBoard', models.BooleanField(verbose_name='Standing Member of Review Boards for Funding Agencies')),
                ('adhocService', models.BooleanField(verbose_name='Ad hoc Service as Referee of Proposals')),
                ('consulting', models.BooleanField(verbose_name='Consulting Activities')),
                ('communityService', models.BooleanField(verbose_name='Community Service')),
            ],
            options={
                'verbose_name': 'Professional and Public Service',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('employment_id', models.AutoField(primary_key=True, serialize=False)),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('position_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TeachingAward',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateField(verbose_name='Start Date')),
                ('enddate', models.DateField(verbose_name='End Date')),
                ('dateinput', models.CharField(blank=True, max_length=30, verbose_name='Custom Date Input')),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Teaching Award',
            },
        ),
        migrations.CreateModel(
            name='TeachingInnovation',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateField(verbose_name='Start Date')),
                ('enddate', models.DateField(verbose_name='End Date')),
                ('dateinput', models.CharField(blank=True, max_length=30, verbose_name='Custom Date Input')),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Teaching Innovation',
            },
        ),
        migrations.CreateModel(
            name='UCICourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('courseNumber', models.CharField(max_length=15, verbose_name='Course Number')),
                ('courseTitle', models.CharField(max_length=30, verbose_name='Course Title')),
                ('enrollment', models.IntegerField()),
                ('numInstructors', models.IntegerField(verbose_name='Number of Instructors')),
                ('percentTaught', models.IntegerField(verbose_name='Percent Taught')),
                ('coreCourse', models.BooleanField(verbose_name='Core Course')),
            ],
            options={
                'verbose_name': 'UCI Course',
            },
        ),
        migrations.CreateModel(
            name='UndergradResearch',
            fields=[
                ('internalID', models.AutoField(primary_key=True, serialize=False)),
                ('startyear', models.IntegerField(verbose_name='Start Year')),
                ('endyear', models.IntegerField(verbose_name='End Year')),
                ('endpresent', models.BooleanField(verbose_name='Until Present?')),
                ('studentName', models.CharField(max_length=100, verbose_name='Student Name')),
                ('role', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('comments', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'verbose_name': 'Undergraduate Student Research Supervision',
            },
        ),
        migrations.CreateModel(
            name='UniversitySystemwide',
            fields=[
                ('employment_id', models.AutoField(primary_key=True, serialize=False)),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('position_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddConstraint(
            model_name='ucicourse',
            constraint=models.UniqueConstraint(fields=('quarter', 'year'), name='quarter_year_pair'),
        ),
    ]
