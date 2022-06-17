"""."""
from django.db import models

# Create your models here.


class Topics(models.Model):
    """."""

    name = models.CharField(max_length=80)

    def __str__(self):
        """."""
        return self.name


class Question(models.Model):
    """."""

    question_text = models.CharField(max_length=800)
    topics = models.ForeignKey(Topics, on_delete=models.CASCADE)

    def __str__(self):
        """."""
        return self.question_text

    def get_questions(self, topics):
        """."""
        print(self.objects.filter(topics=topics))


class Choice(models.Model):
    """."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    def __str__(self):
        """."""
        return self.choice_text
