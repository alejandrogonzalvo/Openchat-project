from django.db import models
from django.contrib.auth.models import User


class Conversation(models.Model):
    name = models.CharField(max_length=30, unique=True, default="Void")
    users = models.ManyToManyField(User)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        to_field="username",
        related_name="author",
        )

    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.CharField(max_length=999)
    date = models.DateTimeField(auto_now=True)
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        to_field="name"
        )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        to_field="username",
        )

    def __str__(self):
        if len(self.text) <= 20:
            return "\n{} // sent {}\n".format(
                self.text,
                self.date
                )

        return "\n{}... // sent {}\n".format(
            self.text[:20],
            self.date
            )
