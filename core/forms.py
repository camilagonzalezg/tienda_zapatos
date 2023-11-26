from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    asunto = forms.CharField(max_length=50)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
    cc_ami = forms.BooleanField(required=False)