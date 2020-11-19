from django.db import models
from multiselectfield import MultiSelectField

from users.models import User

CATEGORY_CHOICES = [
    'Новости недвижимости'
    'Жилая недвижимость'
    'Коммерческая недвижимость'
    'Загородная недвижимость'
    'Зарубежная недвижимость'
    'Новостройки'
    'Вторичное жилье'
    'Строительство'
    'Ремонт квартир'
    'Отделка помещений'
    'Строительные материалы'
    'Дизайн квартир'
    'Проектирование помещений'
    'Инвестиции в недвижимость'
    'Законодательство о недвижимости'
    'Ипотека'
    'Реновация']

class Subscription(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        app_label = 'subscription'


class SubscriptionRelation(models.Model):
    category = models.ManyToManyField(Subscription)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Subscribed')

    def __str__(self):
        return f'User: {self.user} | Categories:{self.category}'
