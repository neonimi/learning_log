from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
	"""新しいユーザーを追加する"""
	if request.method != 'POST':
		form = UserCreationForm() #空のユーザーフォーム
	else:
		form = UserCreationForm(data=request.POST) #入力済フォーム
		if form.is_valid():
			new_user = form.save()
			login(request, new_user)
			return redirect('learning_logs:index')
	context = {'form':form}
	return render(request, 'registration/register.html', context)

def logout(request):
	return render(request, 'registration/logged_out.html')