from django.db import models
from django.urls import reverse


class Season(models.Model):
    title = models.CharField(max_length=255, verbose_name='Год')
    content = models.TextField(blank=True, verbose_name='Содержание страницы')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('season_number', kwargs={'season_number': self.pk})

    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'
        ordering = ['-title']



class Driver(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    content = models.TextField(blank=True, verbose_name='Содержание страницы')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    team_name = models.TextField(blank=True, verbose_name='Команды')
    is_driving = models.BooleanField(default=True, verbose_name='Действующий')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('driver_name', kwargs={'driver_name': self.pk})

    class Meta:
        verbose_name = 'Гонщика'
        verbose_name_plural = 'Гонщики'
        ordering = ['name']


class Team(models.Model):
    team = models.CharField(max_length=255, verbose_name='Команда')
    content = models.TextField(blank=True, verbose_name='Содержание страницы')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    drivers = models.TextField(blank=True, verbose_name='Гонщики')
    is_existing = models.BooleanField(default=True, verbose_name='Существует')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.team

    def get_absolute_url(self):
        return reverse('team_name', kwargs={'team_name': self.pk})

    class Meta:
        verbose_name = 'Команду'
        verbose_name_plural = 'Команды'
        ordering = ['team']

class Track(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    country = models.CharField(max_length=50, verbose_name='Страна')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    content = models.TextField(blank=True, verbose_name='Содержание страницы')
    in_calendar = models.BooleanField(default=True, verbose_name='Участвует')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_track', kwargs={'track_name': self.pk})

    class Meta:
        verbose_name = 'Трассу'
        verbose_name_plural = 'Трассы'
        ordering = ['name']

class Story(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Содержание страницы')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_story', kwargs={'story_number': self.pk})

    class Meta:
        verbose_name = 'Историю'
        verbose_name_plural = 'Истории'
        ordering = ['time_create']

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Содержание страницы')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_news', kwargs={'news_number': self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-time_create']