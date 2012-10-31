from django.db import models

class Post(models.Model):
    """A model for a post in a blog application"""

    title = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    """A model for a comment in a blog post"""

    author = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField('date published')
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return unicode('%s: %s' % (self.post, self.body[:50]))
