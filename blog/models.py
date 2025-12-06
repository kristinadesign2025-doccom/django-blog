from django.db import models


class Review(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(verbose_name='Текст отзыва')
    is_verified = models.BooleanField(default=False, verbose_name='Проверено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_name} - {self.email}'
