"""."""
from django.db import models

# Create your models here.


class Question(models.Model):
    """."""

    question_text = models.CharField(max_length=800)

    def __str__(self):
        """."""
        return self.question_text


class Choice(models.Model):
    """."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    def __str__(self):
        """."""
        return self.choice_text


class Topics(models.Model):
    """."""

    name = models.CharField(max_length=80)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
