from django.db import models


class Task(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовoк задачи"        
        )
    description = models.TextField(
        verbose_name="Описание для задачи"
        )
    completed = models.BooleanField(
        default=False,
        verbose_name="Статус выполнения"
        )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания задачи"
        )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
