from django.forms import ModelForm
from .models import Feedback, Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        # fields = "__all__"
        fields = ['name', 'email', 'subject', 'body']

    def __init__(self,*args,**kwargs):
        super(MessageForm, self).__init__(*args,**kwargs);
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['subject'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control'})


class feedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

    def __init__(self,*args,**kwargs):
        super(feedbackForm, self).__init__(*args,**kwargs);
        self.fields['rating'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['body'].widget.attrs.update(
            {'class': 'form-control'})