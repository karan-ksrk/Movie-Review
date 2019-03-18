from django.db import models



choice = (
    ('Bollywood','Bollywood'),
    ('Hollywood','Hollywood'),
    ('Pollywood','Pollywood'),
    ('Tollywood','Tollywood'),
)
class category(models.Model):
    name = models.CharField(max_length=30, choices=choice)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name


class Movies(models.Model):
    class Meta:
        verbose_name_plural = 'Movies'
    Name = models.CharField(max_length=100, default='')
    Image = models.ImageField(upload_to='image/',null=True, blank=True)
    Subtitle = models.CharField(max_length=50,default='')
    Director = models.CharField(max_length=50,default='')
    Genre = models.CharField(max_length=50,default='')
    Review = models.TextField(max_length=500,default='')
    Category = models.ForeignKey(category, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.Name