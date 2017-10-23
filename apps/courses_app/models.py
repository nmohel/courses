from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 5:
            errors['title'] = "Course title must be at least 5 characters"
        if len(postData['description']) < 1:
            errors['description'] = "Course description must be at least 15 characters"
        return errors

class Course(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CourseManager()