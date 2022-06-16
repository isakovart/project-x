from django.db import models

class Fact(models.Model):
    Name = models.CharField('Name', max_length=255)
    Content = models.TextField('Content')

    def __str__(self) -> str:
        return self.Name

    class Meta:
        verbose_name = 'Fact'
        verbose_name_plural = 'Facts'

class Award(models.Model):
    Name = models.CharField('Name', max_length=255)
    Date = models.DateField('Date')

    def __str__(self) -> str:
        return self.Name

    class Meta:
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'

class Swimmer(models.Model):
    Name = models.CharField('Name', max_length=255)
    Age = models.IntegerField('Age')
    Weight = models.IntegerField('Weight')
    Awards = models.ManyToManyField(Award, verbose_name='Awards')
    Facts = models.ManyToManyField(Fact, verbose_name='Facts')

    def __str__(self) -> str:
        return self.Name

    class Meta:
        verbose_name = 'Swimmer'
        verbose_name_plural = 'Swimmers'