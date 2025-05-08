from django.db import models

# Create your models here.
#班级信息表
class ClaInfo(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

#年级信息表
class GraInfo(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

#学生信息表 必须要继承的对象是models.Model
class StuInfo(models.Model):
    name = models.CharField(max_length=10) # name 为字符串，长度为10
    age = models.IntegerField()
    gender = models.BooleanField()
    is_clainfo = models.ForeignKey(ClaInfo, on_delete=models.CASCADE)
    is_grainfo = models.ForeignKey(GraInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name, self.age, self.gender, self.is_grainfo, self.is_clainfo