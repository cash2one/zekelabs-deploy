from django.db import models

# Create your models here.

from django.db import models
from mezzanine.generic.fields import CommentsField
from mezzanine.generic.fields import RatingField
from django.core.urlresolvers import reverse

class RegisterProfile(models.Model):
    # user = models.OneToOneField("auth.User")
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    mobile = models.CharField(max_length=15,null=True)
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __unicode__(self):
        return self.subject + ' ' + self.mobile

class RegisterCourse(models.Model):
    # user = models.OneToOneField("auth.User")
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    mobile = models.CharField(max_length=15,null=True)
    message = models.TextField()

    def __unicode__(self):
        return self.subject + ' ' + self.mobile

class Courses(models.Model):
	level = (
		('Micro','micro'),
		('Foundation','foundation'),
		('Advance','advance'),
		)

	title = models.CharField(max_length=70)
	slug = models.CharField(max_length=20)
	trainer = models.CharField(max_length=20)
	sme = models.CharField(max_length=20)
	level = models.CharField(max_length=10,choices=level)
	overview = models.TextField()
	content = models.TextField()
	image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
	small_image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
	duration = models.CharField(max_length=10)
	ongoing_batch=models.DateTimeField(auto_now=False)
	upcomming_batch=models.DateTimeField(auto_now=False)
        comments = CommentsField()
        rating = RatingField()

	def __unicode__(self):
		return self.title + ' ' + self.overview      

        def get_absolute_url(self):
                return reverse('home', kwargs={})

class Event(models.Model):
        level = (
                ('Micro','micro'),
                ('Foundation','foundation'),
                ('Advance','advance'),
                )
        title = models.CharField(max_length=70)
        couponcode = models.CharField(max_length=10)
        slug = models.CharField(max_length=20)
        trainer = models.CharField(max_length=20)
        sme = models.CharField(max_length=20)
        level = models.CharField(max_length=10,choices=level)
        overview = models.TextField()
        content = models.TextField()
        image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
        duration = models.CharField(max_length=10)
        comments = CommentsField()
        participants = models.IntegerField()


        def __unicode__(self):
               return self.title + ' ' + self.overview

class AdvCourses(models.Model):
        title = models.CharField(max_length=70)
        comments = CommentsField()

        def __unicode__(self):
                return self.title

class SubjectMatterExpert(models.Model):
       name = models.CharField(max_length=70)
       profile = models.TextField()
       image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
       subjects = models.TextField()
