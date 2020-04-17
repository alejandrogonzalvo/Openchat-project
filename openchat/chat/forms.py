from django import forms
from .models import Conversation, Message


class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ['name', 'users']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
