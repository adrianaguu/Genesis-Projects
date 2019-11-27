from django import forms

from inscripcion.models import Inscripcion
from actividad.models import Actividad
from reportes.models import ControlAsistencia, ControlMaterial
from material.models import Material


class InscripcionForm(forms.ModelForm):


    codigo_descuento = forms.CharField(required=False)

    def __init__(self,evento,*args,**kwargs):
        super (InscripcionForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['actividades'] = forms.ModelMultipleChoiceField(queryset=Actividad.objects.filter(evento=evento),
            widget=forms.CheckboxSelectMultiple,
            required=True)
        self.fields['actividades'].widget.attrs.update({'class' : 'myCheckbox'})
        
        #self.fields['actividades'].queryset = Actividad.objects.filter(evento=evento)

    class Meta:
        model = Inscripcion
        exclude = ('evento','monto','dia_hora_asistencia',)

class ControlAsistenciaForm(forms.ModelForm):
    def __init__(self,evento,*args,**kwargs):
        super (ControlAsistenciaForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['asistentes'] = forms.ModelMultipleChoiceField(queryset=Inscripcion.objects.filter(evento=evento),
            widget=forms.CheckboxSelectMultiple,
            required=True)
        self.fields['asistentes'].widget.attrs.update({'class' : 'myCheckbox'})
        
        #self.fields['actividades'].queryset = Actividad.objects.filter(evento=evento)

    class Meta:
        model = ControlAsistencia
        exclude = ('evento',)

class ControlMaterialForm(forms.ModelForm):
    def __init__(self,actividad,*args,**kwargs):
        super (ControlMaterialForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['materiales'] = forms.ModelMultipleChoiceField(queryset=Material.objects.filter(actividad=actividad),
            widget=forms.CheckboxSelectMultiple,
            required=True)
        self.fields['materiales'].widget.attrs.update({'class' : 'myCheckbox'})
        
        #self.fields['actividades'].queryset = Actividad.objects.filter(evento=evento)

    class Meta:
        model = ControlMaterial
        exclude = ('actividad',)




        