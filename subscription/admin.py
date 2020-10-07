from django.contrib import admin

from .models import Subscription, SubscriptionRelation

class SubscriptionRelationAdmin(admin.ModelAdmin):
    list_display = ('user', )
    filter_horizontal = ()
    search_fields = ('user', )

admin.site.register(Subscription)
admin.site.register(SubscriptionRelation, SubscriptionRelationAdmin)