from django.db import models

from users.models import User


# CATEGORY_CHOICES = (
#     ('1', 'Новости недвижимости'),
#     ('2', 'Жилая недвижимость'),
#     ('3', 'Коммерческая недвижимость'),
#     ('4', 'Загородная недвижимость'),
#     ('5', 'Зарубежная недвижимость'),
#     ('6', 'Новостройки'),
#     ('7', 'Вторичное жилье'),
#     ('8', 'Строительство'),
#     ('9', 'Ремонт квартир'),
#     ('10', 'Отделка помещений'),
#     ('11', 'Строительные материалы'),
#     ('12', 'Дизайн квартир'),
#     ('13', 'Проектирование помещений'),
#     ('14', 'Инвестиции в недвижимость'),
#     ('15', 'Законодательство о недвижимости'),
#     ('16', 'Ипотека'),
#     ('17', 'Реновация')
# )
class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Posting(models.Model):

    categories = models.ManyToManyField(
        Category,
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='my_posts')
    paid_content = models.BooleanField(default=False)
    who_liked = models.ManyToManyField(User, through='UserPostRelation'
                                       , related_name='liked')

    #Posts Images
class PostImage(models.Model):
    post = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='post_image')
    images = models.ImageField(upload_to='post_image/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Posting:{self.post} | Images {self.images}'



# /////// USER (LIKES AND SAVES) TO POST RELATION ////////



class UserPostRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.OneToOneField(Posting, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)
    reacted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Owner{self.user}, Post:{Posting.title}'

