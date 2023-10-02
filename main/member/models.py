from django.db import models

# Create your models here.


class Student(models.Model):
      name = models.CharField(max_length=200)
      age = models.IntegerField(blank=True, null=True)
      roll = models.IntegerField(blank=True, null=True)
      deprt = models.CharField(max_length=200,blank=True, null=True)

      class Meta:
            verbose_name_plural ='Student'

      def __str__(self):
            return self.name


class Teacher(models.Model):
      name = models.CharField(max_length=200)
      department = models.CharField(max_length=200 , blank=True, null=True)
      email = models.EmailField(max_length=120, blank=True, null=True)

      class Meta:
            verbose_name_plural ='Teacher'

      def __str__(self):
            return self.name
