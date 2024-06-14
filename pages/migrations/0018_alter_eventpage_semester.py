# Generated by Django 3.2.5 on 2021-07-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_remove_eventpage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='semester',
            field=models.CharField(blank=True, choices=[('ws-2024', 'Wintersemester 2024/2025'), ('sos-2024', 'Sommersemester 2024'), ('ws-2023', 'Wintersemester 2023/2024'), ('sos-2023', 'Sommersemester 2023'), ('ws-2022', 'Wintersemester 2022/2023'), ('sos-2022', 'Sommersemester 2022'), ('ws-2021', 'Wintersemester 2021/2022'), ('sos-2021', 'Sommersemester 2021'), ('ws-2020', 'Wintersemester 2020/2021'), ('sos-2020', 'Sommersemester 2020'), ('ws-2019', 'Wintersemester 2019/2020'), ('sos-2019', 'Sommersemester 2019'), ('ws-2018', 'Wintersemester 2018/2019'), ('sos-2018', 'Sommersemester 2018'), ('ws-2017', 'Wintersemester 2017/2018'), ('sos-2017', 'Sommersemester 2017'), ('ws-2016', 'Wintersemester 2016/2017'), ('sos-2016', 'Sommersemester 2016'), ('ws-2015', 'Wintersemester 2015/2016'), ('sos-2015', 'Sommersemester 2015'), ('ws-2014', 'Wintersemester 2014/2015'), ('sos-2014', 'Sommersemester 2014'), ('ws-2013', 'Wintersemester 2013/2014'), ('sos-2013', 'Sommersemester 2013'), ('ws-2012', 'Wintersemester 2012/2013'), ('sos-2012', 'Sommersemester 2012'), ('ws-2011', 'Wintersemester 2011/2012'), ('sos-2011', 'Sommersemester 2011'), ('ws-2010', 'Wintersemester 2010/2011'), ('sos-2010', 'Sommersemester 2010')], default='ss2021', max_length=255),
        ),
    ]