from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=255, unique=True, verbose_name='Название отеля')
    stars_count = models.IntegerField(verbose_name='Количество звёзд', default=0)
    country = models.CharField(max_length=40, verbose_name='Страна')
    hotel_phone = models.CharField(max_length=255, verbose_name='Контакты')
    hotel_mail = models.EmailField(verbose_name='Почта отеля')
    pool = models.BooleanField(default=False, verbose_name='Наличие бассейна')
    beach = models.BooleanField(default=False, verbose_name='Наличие пляжа(рядом)')
    bar_free = models.BooleanField(default=False, verbose_name='Наличие бесплатного бара')
    photo = models.ImageField(verbose_name='Фото отеля', upload_to='photos')

    def __str__(self):
        return self.hotel_name

    class Meta:
        ordering = ['hotel_name']


class Tour(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Отель')
    country = models.CharField(max_length=40, verbose_name='Страна')
    tour_name = models.CharField(max_length=255, unique=True, verbose_name='Название тура')
    tour_start = models.DateTimeField(verbose_name='Начало тура')
    tour_finish = models.DateTimeField(verbose_name='Конец тура')
    count_of_days = models.SmallIntegerField(verbose_name='Количество дней', default=0)
    price = models.IntegerField(verbose_name='Цена', default=0)
    departure_point = models.CharField(max_length=40, verbose_name='Место отправления')
    count_of_free_place = models.IntegerField(verbose_name='Количество свободных мест', default=0)
    photo = models.ImageField(verbose_name='Фото тура', upload_to='photos')

    def __str__(self):
        return self.tour_name


class Article(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название статьи')
    photo = models.ImageField(verbose_name='Фото статьи', upload_to='photos')

    def __str__(self):
        return self.name


class Message(models.Model):
    chat = models.ForeignKey(
        Hotel,
        verbose_name='Комментарии отелей',
        on_delete=models.CASCADE)

    author = models.ForeignKey(
        User,
        verbose_name='Пользователь', on_delete=models.CASCADE)

    message = models.TextField('Комментарий')
    pub_date = models.DateTimeField(
        'Дата Комментария',
        default= timezone.now)


class Order(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=255)
    surname = models.CharField(verbose_name="Фамилия", max_length=255)
    mail = models.EmailField(verbose_name="Почта")
    phone = models.CharField(verbose_name="Телефон", max_length=255)
    place = models.IntegerField(verbose_name="Количество мест")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Тур')