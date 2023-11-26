from django import forms

class FormularioContacto(forms.Form):
    asunto = forms.CharField(max_length=50)
    email = forms.EmailField()
    nombre = forms.CharField(max_length=50)
    mensaje = forms.CharField(widget=forms.Textarea)
    cc_ami = forms.BooleanField(required=False)