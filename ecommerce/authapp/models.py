from django.db import models
class Register(models.Model):
    fname=models.CharField(max_length=20)
    phno=models.IntegerField()
    email=models.EmailField()
    uname=models.CharField(primary_key=True,max_length=20)
    pwd=models.CharField(max_length=15)
    cpwd=models.CharField(max_length=15)
    def get_fname(self):
        return self.fname
    #def get_phno(self):
        #return self.phno
    #def get_email(self):
       # return self.email
    #def get_uname(self):
        #return self.uname
    #def get_pwd(self):
        #return self.pwd
    #def get_cpwd(self):
        #return self.cpwd
class login(models.Model):
    username=models.CharField(primary_key=True,max_length=10)
    password=models.CharField(max_length=20)

    def get_user(self):
        return self.username
    def get_pswd(self):
        return self.password