from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank = True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now = True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Женщина'
        verbose_name_plural = 'Женщины'

class Category(models.Model):
    name = models.CharField(max_length=100,db_index = True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'




    def __str__(self):
        return self.name
