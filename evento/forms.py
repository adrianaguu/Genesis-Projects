from django import forms

from inscripcion.models import Inscripcion
from actividad.models import Actividad


class InscripcionForm(forms.ModelForm):
    def __init__(self,evento,*args,**kwargs):
        super (InscripcionForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['actividades'] = forms.ModelMultipleChoiceField(queryset=Actividad.objects.filter(evento=evento),
            widget=forms.CheckboxSelectMultiple,
            required=True)
        self.fields['actividades'].widget.attrs.update({'class' : 'myCheckbox'})
        
        #self.fields['actividades'].queryset = Actividad.objects.filter(evento=evento)

    class Meta:
        model = Inscripcion
        exclude = ('evento','monto',)


        