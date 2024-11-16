from django.db import models
from django.contrib.auth.models import User

# Create an Image Creation Model
class Creations(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    init_img = models.ImageField(blank=True, null=True)
    p_prompt = models.CharField(max_length=255)
    n_prompt = models.CharField(max_length=255)
    generated_img = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user} Img {self.id}'

    class Meta:
        verbose_name_plural = 'Creations'