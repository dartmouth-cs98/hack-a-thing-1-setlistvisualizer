from django import forms

class SearchForm(forms.Form):
	artist = forms.CharField(help_text="Enter an Artist")
	unique = forms.CharField(help_text="Enter unique")
	url_start = forms.CharField(help_text="Enter the start-date URL")
	url_stop = forms.CharField(help_text="Enter the end-date URL")