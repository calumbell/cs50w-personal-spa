from django.db import models
from django.utils import timezone

class BlogCategory(models.Model):
  name = models.CharField(max_length=64)

  def __str__(self):
    return self.name


options = (
  ('draft', 'Draft'),
  ('publicshed', 'Published'),
)

class BlogPost(models.Model):
  category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT)
  title = models.CharField(max_length=256)
  excerpt = models.TextField(null=True)
  content = models.TextField()
  slug = models.SlugField(max_length=256, unique_for_date='published')
  published = models.DateField()
  status = models.CharField(max_length=10, choices=options, default='published')

  class Meta:
    ordering = ('-published',)

  def __str__(self):
    return self.slug