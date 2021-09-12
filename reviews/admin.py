from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Review


@modeladmin_register
class ReviewAdmin(ModelAdmin):
    model = Review
    menu_label = "Reviews"
    menu_icon = "placeholder"
    menu_order = 300
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("content", "rating")
    search_fields = "content"
