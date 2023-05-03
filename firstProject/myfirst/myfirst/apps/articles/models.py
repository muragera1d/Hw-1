from django.db import models

class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=200)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField("Дата публикации")

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    autor_name = models.CharField("Имя автора", max_length=50)
    comment_text = models.CharField("Текст коммента", max_length=200)
