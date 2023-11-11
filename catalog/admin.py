from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language, Publisher, Status
from django.utils.html import format_html


# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Genre)
# admin.site.register(Language)
# admin.site.register(Publisher)
# admin.site.register(Status)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "photo",)
    fields = ['last_name', "first_name", "about", ("date_of_birth", 'photo')]
    readonly_fields = ['show_photo']
    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height:100 px;">')
    show_photo.short_description = "Foto"






admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", 'genre', 'language', "show_photo")
    list_filter = ("genre", "author")
    inlines = [BooksInstanceInline]
    readonly_fields = ['show_photo']
    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style="max-height:100 px;">')
    show_photo.short_description = "Muqova"





@admin.register(BookInstance)
class BookinstanceAdmin(admin.ModelAdmin):
    list_filter = ("book", "status")
    fieldsets = (
        ("Kitob nusxasi", {
            'fields': ("book", "inv_nom")
        }),
        ("Kitobning tugash statusi", {
            "fields": ("status", "due_back")
        }),
    )


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)