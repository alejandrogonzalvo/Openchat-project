from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as do_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


from .models import Message, Conversation
from .forms import ConversationForm


def conversation_list(request):
    if request.user.is_authenticated:
        conversations = Conversation.objects.filter(
            users=request.user
            )
        return render(
            request,
            'chat/conversation_list.html',
            {'conversations': conversations}
            )

    return HttpResponseRedirect('')


def message_list(request, conversation):
    messages = Message.objects.filter(conversation=conversation)
    return render(
        request,
        'chat/message_list.html',
        {'messages': messages, 'user': request.user},
        )


def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        form.is_valid()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            do_login(request, user)
            return HttpResponseRedirect('conversations')

    else:
        form = AuthenticationForm()

    return render(request, 'chat/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            do_login(request, user)
            return HttpResponseRedirect('conversations')

    else:
        form = UserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})


def create_conversation(request):
    if request.method == 'POST':
        form = ConversationForm(request.POST)
        if form.is_valid():
            new_conversation = Conversation.objects.create(
                name=form.cleaned_data['name'],
                author=request.user,
                )
            new_conversation.users.set(form.cleaned_data['users'])
            new_conversation.save()
            return HttpResponseRedirect(
                '{}'.format(new_conversation.name)
                )

    else:
        form = ConversationForm(request.POST)
    return render(request, 'chat/create_conversation.html', {'form': form})
