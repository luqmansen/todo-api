from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Notes(BaseModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    deadline = models.DateTimeField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
