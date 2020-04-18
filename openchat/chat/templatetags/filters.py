from django import template
from django.template.defaulttags import register


register = template.Library()

@register.filter
def messages_by_conversation(messages, conversation):
    filtered_list = [message for message in messages if message.conversation == conversation]
    return filtered_list