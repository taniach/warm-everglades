from django import forms
from .models import Category, Product
from django.utils.safestring import mark_safe
from string import Template

class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        html =  Template("""<img src="../$link"/ height="300" width="300">""")
        return mark_safe(html.substitute(link=value))

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name', 'icon']
			
		