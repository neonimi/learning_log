from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import TopicForm, EntryForm
from django.http import Http404

# Create your views here.
def index(request):
	return render(request, 'learning_logs/index.html')

@login_required
def topic(request):
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topic': topics}
	return render(request, 'learning_logs/topic.html', context)

@login_required
def topic_child(request, topic_id):
	"""１つのトピックとそれについての全ての記事を表示"""
	topic = Topic.objects.get(id=topic_id)
	# トピックが現在のユーザーが所持するものであることを確認する
	if topic.owner != request.user:
		raise Http404

	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, "learning_logs/topic_child.html", context)

@login_required
def new_topic(request):
	if request.method != 'POST':#データ送信されていない時
		form = TopicForm()#空のフォーム
	else:#データ送信された時
		form = TopicForm(data=request.POST)#データ入りフォーム
		if form.is_valid():#バリデーション
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()#保存
			return redirect('learning_logs:topic')#保存後の画面表示先
	context = {'form': form}#フォームを送る
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	# 記事が現在のユーザーが所持するものであることを確認する
	if topic.owner != request.user:
		raise Http404
	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return redirect('learning_logs:topic_child', topic_id=topic_id)
	context = {'topic': topic,'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit(request, entry_id):
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	# トピックが現在のユーザーが所持するものであることを確認する
	if topic.owner != request.user:
		raise Http404

	if request.method != 'POST':
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid:
			form.save()
			return redirect('learning_logs:topic_child', topic_id=topic.id)

	context = {'entry': entry, 'topic':topic ,'form':form}
	return render(request, 'learning_logs/edit.html', context)
