from django.urls import path


from . import views

app_name = 'chat'
urlpatterns = [
    path(
        '',
        views.login,
        name="login"
        ),
    path(
        'conversations',
        views.conversation_list,
        name='conversation_list'
        ),
    path(
        'conversations/create-conversation',
        views.create_conversation,
        name='create_conversation'
    ),
    path(
        'conversations/<conversation>',
        views.message_list,
        name='message_list'
        ),
    path(
        'signup',
        views.signup
    ),
]
