from django import forms
from .models import Task
from django.utils.translation import ugettext
from django.forms.extras.widgets import SelectDateWidget

class TaskForm(forms.ModelForm):
	# start_date = forms.DateField(widget=SelectDateWidget)
	# end_date = forms.DateField(widget=SelectDateWidget)
	class Meta:
		model = Task
		fields = ['name','start_date', 'end_date', 'status']
		widgets = {
			'name':forms.TextInput(
				attrs={'id':'post-text', 'required': True, 'placeholder': 'Say something...'}
				),
			'start_date':forms.TextInput(
				attrs={'id':'start_date', 'placeholder': '0000-00-00'}
				),
			'end_date':forms.TextInput(
				attrs={'id':'end_date', 'placeholder': '0000-00-00'}
				),
		}