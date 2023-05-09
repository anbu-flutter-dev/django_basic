from django.db import models


class Play(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

class PlayModels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    main_play = models.ForeignKey(Play, on_delete=models.CASCADE, related_name= 'play')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
