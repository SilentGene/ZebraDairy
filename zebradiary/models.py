from django.db import models

class Topic(models.Model):
	'''用户学习的主题'''
	text = models.CharField(max_length = 25)
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		'''返回模型的字符串表示'''
		return self.text

class Entry(models.Model):
	'''某个主题下具体的内容'''
	#外键是数据库术语，它引用了数据库中的另一条记录；这些代码将每个条目关联到特定的主题。
	#每个主题创建时，都给他分配了一个键ID。
	#需要在两项数据之间建立联系时，Django使用与每项信息相关联的键
	topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		'''返回模型的字符串表示'''
		return self.text[:50] + "..."