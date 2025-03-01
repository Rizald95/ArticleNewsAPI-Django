from django.db import models

class Article(models.Model):
    SECTION_CHOICES = [
        ('featured', 'Featured'),
        ('sidebar', 'Sidebar'),
        ('bottom', 'Bottom'),
    ]
    
    CATEGORY_CHOICES = [
        ('Space and Universe', 'Space and Universe'),
        ('Our Planet', 'Our Planet'),
        ('Technology', 'Technology'),
        ('Health and Science', 'Health and Science'),
        ('Opinion', 'Opinion'),
        ('News', 'News'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    read_time = models.IntegerField(default=5)  # in minutes
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    section = models.CharField(max_length=20, choices=SECTION_CHOICES, default='bottom')
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_date']