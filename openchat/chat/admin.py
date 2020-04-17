from django.contrib import admin


from .models import Conversation, Message


class MessageInLine(admin.TabularInline):
    model = Message
    extra = 0
class ConversationAdmin(admin.ModelAdmin):
    inlines = [MessageInLine]


admin.site.register(Conversation, ConversationAdmin)
