from django.contrib import admin
from orders.models import PurchaseItem, Purchase


class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 1
    readonly_fields = ('get_item_title',)

    def get_item_title(self, obj):
        return str(obj.content_object)
    get_item_title.short_description = 'Item Title'


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'get_total_price')
    inlines = [PurchaseItemInline]

    def get_total_price(self, obj):
        return obj.get_total_price()
    get_total_price.short_description = 'Total Price'

admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseItem)