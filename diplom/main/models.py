from django.db import models

class md_chapter(models.Model):
    id_chapter = models.AutoField(primary_key=True)
    chapter = models.CharField(max_length=50)

    class Meta:
        app_label = 'main'
        managed = False
        db_table = 'md_chapter'
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


    def __str__(self):
        return self.chapter

    def get_absolute_url(self):
        return '/home/chapter'

class MdDivision(models.Model):
    id_division = models.AutoField(primary_key=True)
    division = models.CharField(max_length=50)

    class Meta:
        app_label = 'main'
        managed = False
        db_table = 'md_division'
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.division

    def get_absolute_url(self):
        return '/home/division'

class MdMethodicalSolution(models.Model):
    id_methodical_solution = models.AutoField(primary_key=True)
    id_chapter = models.ForeignKey(md_chapter, models.DO_NOTHING, db_column='id_chapter')
    id_responsible = models.ForeignKey('MdResponsible', models.DO_NOTHING, db_column='id_responsible')
    id_division = models.ForeignKey(MdDivision, models.DO_NOTHING, db_column='id_division')
    id_period = models.ForeignKey('MdPeriod', models.DO_NOTHING, db_column='id_period')
    decision = models.CharField(max_length=150)
    note = models.CharField(max_length=75)
    marks_of_completion = models.CharField(max_length=20)
    reason_for_nonfulfillment = models.CharField(max_length=75)
    md_date = models.DateField()  # This field type is a guess.

    def get_absolute_url(self):
        return '/home/'

    class Meta:
        app_label = 'main'
        managed = False
        db_table = 'md_methodical_solution'
        verbose_name = 'Методическое решение'
        verbose_name_plural = 'Методические решения'


class MdPeriod(models.Model):
    id_period = models.AutoField(primary_key=True)
    period = models.CharField(max_length=21)

    class Meta:
        app_label = 'main'
        managed = False
        db_table = 'md_period'
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'

    def __str__(self):
        return self.period

    def get_absolute_url(self):
        return '/home/period'

class MdResponsible(models.Model):
    id_responsible = models.AutoField(primary_key=True)
    responsible = models.CharField(max_length=50)

    class Meta:
        app_label = 'main'
        managed = False
        db_table = 'md_responsible'
        verbose_name = 'Ответстыенный'
        verbose_name_plural = 'Ответстыенные'

    def __str__(self):
        return self.responsible

    def get_absolute_url(self):
        return '/home/responsible'

