from django.db import models
import re

class Todo(models.Model):
    todo_text = models.CharField(max_length=50)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    def __str__(self):
        return self.todo_text

    def is_todo_contain_words(self):
        return True if re.match(r'[a-zA-Z]+\w', self.todo_text) else False
