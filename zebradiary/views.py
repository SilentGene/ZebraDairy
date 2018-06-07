from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
	'''主页'''
	topics = Topic.objects.order_by('text')
	context = {'topics': topics}
	return render(request, 'zebradiary/index.html', context)

def topics(request):
	topics = Topic.objects.order_by('text')
	context = {'topics': topics}
	return render(request, 'zebradiary/topics.html', context)

def topic(request, topic_id):#这个函数有第二个形参，接收从urls.py捕获的值，并存储到topic_id中
	'''显示单个主题及其所有条目'''
	topic = Topic.objects.get(id = topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'zebradiary/topic.html', context)

def new_entry(request, topic_id):
	'''在特定的主题中添加新条目'''
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		#如果是get，未提交数据则创建空表单
		form = EntryForm()
	else:
		#POST提交的数据，对数据进行处理
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			#将用户重定向到显示相关主题的页面
			return HttpResponseRedirect(reverse('zebradiary:topic',
										args=[topic_id]))
	context = {'topic':topic, 'form':form}
	return render(request, 'zebradiary/new_entry.html', context)

