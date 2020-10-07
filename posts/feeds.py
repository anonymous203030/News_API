from django.contrib.gis.feeds import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse

from .models import Posting


class LatestEntriesFeed(Feed):
    title = "Узнавайте Все Новости Первыми!"
    link = "latest/feeds/rss/"
    description = "Все Новые Новости Будут Всегда С Вами!"

    def items(self, request):
        return Posting.objects.order_by('-created_at').filter(paid_content=False)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)

    def item_link(self, item):
        return reverse('news-item')
