from django.contrib import admin, messages
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect

from racks.models import Rack, Book

# Register your models here.


class BookAdminInline(admin.StackedInline):
    model = Book
    extra = 1


class RacksAdmin(admin.ModelAdmin):
    list_display = ['name', '_books', '_total_books']
    # readonly_fields = ['slug']

    inlines = [BookAdminInline]

    def _books(self, obj):
        books = [book.title for book in obj.book_set.all()]
        return ' | '.join(books)

    def _total_books(self, obj):
        return obj.book_set.all().count()

    def save_formset(self, request, form, formset, change):
        try:
            super().save_formset(request, form, formset, change)
        except ValueError as value_error:
            messages.error(request, str(value_error))
            return redirect("admin:racks_rack_changelist")


admin.site.register(Rack, RacksAdmin)
admin.site.unregister([Group, User])