from django import forms

from app.models import *

from django.utils.translation import gettext_lazy
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['url']
        widgets={'name':forms.PasswordInput,'url':forms.Textarea()}
        labels={'name':gettext_lazy('First Name'),'url':gettext_lazy('Url_data')}
        help_texts={'name':gettext_lazy('enter ur name')}
