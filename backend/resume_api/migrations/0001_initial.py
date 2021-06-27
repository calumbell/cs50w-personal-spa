# Generated by Django 3.2 on 2021-06-26 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.CharField(max_length=64)),
                ('label', models.CharField(blank=True, max_length=64, null=True)),
                ('summary', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('subtitle', models.CharField(max_length=64)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField(blank=True, null=True)),
                ('website', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'ordering': ('-startDate',),
            },
        ),
        migrations.CreateModel(
            name='WorkItem',
            fields=[
                ('resumeitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resume_api.resumeitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work', to='resume_api.resume')),
            ],
            bases=('resume_api.resumeitem',),
        ),
        migrations.CreateModel(
            name='EducationItem',
            fields=[
                ('resumeitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resume_api.resumeitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='resume_api.resume')),
            ],
            bases=('resume_api.resumeitem',),
        ),
        migrations.CreateModel(
            name='CPDItem',
            fields=[
                ('resumeitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resume_api.resumeitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cpd', to='resume_api.resume')),
            ],
            bases=('resume_api.resumeitem',),
        ),
    ]
