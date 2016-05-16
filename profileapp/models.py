from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Profile(models.Model):
    name            = models.CharField(max_length=200)
    avatar          = models.ImageField(upload_to='avatar')
    job_name        = models.CharField(max_length=200)
    detail_profile  = models.TextField()

    website         = models.URLField()
    repository      = models.URLField()
    email           = models.EmailField()
    phone           = models.CharField(max_length=200)

    #social media
    facebook        = models.CharField(max_length=200, null=True, blank=True)
    twitter         = models.CharField(max_length=200, null=True, blank=True)
    linkedin        = models.CharField(max_length=200, null=True, blank=True)
    google_plus     = models.CharField(max_length=200, null=True, blank=True)
    iframe_maps     = models.TextField()

    def __unicode__(self):
        return self.name

class Job_Experience(models.Model):
    profile         = models.ForeignKey(Profile, related_name='job_experience')
    company_name    = models.CharField(max_length=200)
    job_detail      = models.CharField(max_length=200)

class Education(models.Model):
    profile         = models.ForeignKey(Profile, related_name='education')
    education_name  = models.CharField(max_length=200)
    detail_education= models.CharField(max_length=200)

class Awards(models.Model):
    profile         = models.ForeignKey(Profile, related_name='awards')
    award_name      = models.CharField(max_length=200)
    detail_award    = models.CharField(max_length=200)

class Resume(models.Model):
    profile         = models.ForeignKey(Profile, related_name='resume')
    resume_name     = models.CharField(max_length=200)
    detail_resume   = models.CharField(max_length=200)

class Portfolio(models.Model):
    profile         = models.ForeignKey(Profile, related_name='portfolio')
    project_name    = models.CharField(max_length=200)
    project_link    = models.URLField(max_length=200, null=True, blank=True)
    project_image   = models.ImageField(upload_to='projects')
    project_detail  = models.TextField(blank=True)

class Skills(models.Model):
    profile         = models.ForeignKey(Profile, related_name='skills')
    skill_name      = models.CharField(max_length=200)
    skill_score     = models.PositiveIntegerField()
