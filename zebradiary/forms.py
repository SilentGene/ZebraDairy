from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']#该表单只包含字段text
		labels = {'text': ''}#不要为字段text生成标签

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		#设置widgets小部件可覆盖Django选择的默认元素属性
		#定制了字段'text'的输入小部件，将文本区域的宽度设置为80列而不是默认的40列
		widgets = {'text': forms.Textarea(attrs={'class':'form-control'})}
