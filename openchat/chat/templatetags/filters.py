from django import template
from django.template.defaulttags import register


register = template.Library()

@register.filter
def messages_by_conversation(messages, conversation):
    filtered_list = messages.get(conversation.name)
    return filtered_list