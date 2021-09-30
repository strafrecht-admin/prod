# Generated by Django 3.2.5 on 2021-07-26 17:07

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtaildocs', '0012_uploadeddocument'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('pages', '0014_auto_20210726_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('name', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField()),
                ('semester', models.CharField(blank=True, choices=[('2024_2', 'Wintersemester 2024/2025'), ('2024_1', 'Sommersemester 2024'), ('2023_2', 'Wintersemester 2023/2024'), ('2023_1', 'Sommersemester 2023'), ('2022_2', 'Wintersemester 2022/2023'), ('2022_1', 'Sommersemester 2022'), ('2021_2', 'Wintersemester 2021/2022'), ('2021_1', 'Sommersemester 2021'), ('2020_2', 'Wintersemester 2020/2021'), ('2020_1', 'Sommersemester 2020'), ('2019_2', 'Wintersemester 2019/2020'), ('2019_1', 'Sommersemester 2019'), ('2018_2', 'Wintersemester 2018/2019'), ('2018_1', 'Sommersemester 2018'), ('2017_2', 'Wintersemester 2017/2018'), ('2017_1', 'Sommersemester 2017'), ('2016_2', 'Wintersemester 2016/2017'), ('2016_1', 'Sommersemester 2016'), ('2015_2', 'Wintersemester 2015/2016'), ('2015_1', 'Sommersemester 2015'), ('2014_2', 'Wintersemester 2014/2015'), ('2014_1', 'Sommersemester 2014'), ('2013_2', 'Wintersemester 2013/2014'), ('2013_1', 'Sommersemester 2013'), ('2012_2', 'Wintersemester 2012/2013'), ('2012_1', 'Sommersemester 2012'), ('2011_2', 'Wintersemester 2011/2012'), ('2011_1', 'Sommersemester 2011'), ('2010_2', 'Wintersemester 2010/2011'), ('2010_1', 'Sommersemester 2010')], default='ss2021', max_length=255)),
                ('youtube_link', models.CharField(blank=True, max_length=500, null=True)),
                ('type', models.CharField(blank=True, choices=[('tacheles', 'Tacheles'), ('sonstige', 'Sonstige')], default='tacheles', max_length=255)),
                ('description', wagtail.core.fields.RichTextField(blank=True)),
                ('speaker_description', wagtail.core.fields.RichTextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('showmap', models.BooleanField(default=False)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('newsletter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document')),
                ('poster_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('poster_pdf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]
