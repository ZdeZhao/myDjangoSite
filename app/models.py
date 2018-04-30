from django.db import models

# Create your models here.
KIND_CHOICES = (
    ('Python技术', 'Python技术'),
    ('数据库技术', '数据库技术'),
    ('经济学', '经济学'),
    ('文体资讯', '文体资讯'),
    ('个人心情', '个人心情'),
    ('其他', '其他'),
)


class Moment(models.Model):
    content = models.CharField(max_length=300)
    user_name = models.CharField(max_length=20, default='匿名')
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    n_visits = models.IntegerField()

    def __str__(self):
        return self.headline


class Account(models.Model):
    user_name = models.CharField(max_length=80)
    password = models.CharField(max_length=255)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Account: %s" % self.user_name


class Contact(models.Model):
    account = models.ForeignKey("Account", on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=10)
    address = models.CharField(max_length=80)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return "%s, %s" % (self.account.user_name, self.mobile)