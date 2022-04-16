from django.db import models
import uuid
# from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# class Question(models.Model):

#     TYPES = (
#         ('backend', 'backend'),
#         ('frontend', 'frontend'),
#         ('fullstack', 'fullstack'),
#     )

#     answer = models.CharField(max_length=200, choices=TYPES)
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4,  unique=True,
#                           primary_key=True, editable=False)

#     def __str__(self):
#         return self.answer
class Education(models.Model):
    instituteName = models.CharField(max_length=200, null=True)
    degree = models.CharField(max_length=200, null=True)
    stream = models.CharField(max_length=200, null=True)
    score = models.CharField(max_length=200, null=True)
    total = models.CharField(max_length=200, null=True)
    logo = models.ImageField(null=True)
    url = models.CharField(max_length=200, null=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.instituteName


class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    body = models.TextField(null=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)
    github = models.TextField(blank=True,default="#")
    deployLink = models.TextField(blank=True,default="#")
    tags = models.TextField(blank=True,null=True)
    def getTags(self):
        if self.tags: 
            return self.tags.split(",");
        else: return ([]);
    def __str__(self):
        return self.title

# class Comment(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     body = models.TextField(null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return self.body[0:50]


class Skill(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, default="skill.png")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    # rating = models.IntegerField()
    rating = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)
    def __str__(self):
        return self.rating

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)
    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    def __str__(self):
        return self.name

# class Endorsement(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     body = models.TextField()
#     approved = models.BooleanField(default=False, null=True)
#     featured = models.BooleanField(default=False)

#     def __str__(self):
#         return self.body[0:50]