from django import forms #IMPORTAMOS LOS FORMULARIOS
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #IMPORTAMOS EL FORMULARIO DE AUTENTICACIÓN
from django.contrib.auth.models import User #IMPORTAMOS EL MODELO DE USUARIOS
from .models import * #IMPORTAMOS LOS MODELOS
from accounts.models import Profile, Region, Comuna


#FORMULARIO LOGIN
class LoginForm(AuthenticationForm):
    pass



#____________________________________________________________________________________________________________________________    
#CREAMOS EL FORMULARIO EL CUAL HEREDA LOS DATOS DEL USER
class UserForm(forms.ModelForm):
    class Meta:
        model = User #IMPORTAMOS EL MODELO DE USUARIOS
        fields = ['first_name', 'email']



#____________________________________________________________________________________________________________________________
#FORMULARIO DE PERFIL

class ProfileForm(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), widget=forms.Select(attrs={'class': 'bg-white text-gray-900 rounded-xl pl-2 py-1 md:py-2 text-sm focus:outline-none w-full'}))
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), widget=forms.Select(attrs={'class': 'bg-white text-gray-900 rounded-xl pl-2 py-1 md:py-2 text-sm focus:outline-none w-full'}))

    class Meta:
        model = Profile
        fields = ['image', 'apellido_paterno', 'apellido_materno', 'direccion', 'region', 'comuna', 'telefono']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'bg-white text-gray-900 rounded-xl pl-2 py-1 md:py-2 text-sm focus:outline-none w-full'
            }),

            'apellido_paterno': forms.TextInput(attrs={
                'class': 'bg-white text-gray-900 rounded-xl pl-2 py-1 md:py-2 text-sm focus:outline-none w-full',
                'placeholder': 'Apellido Paterno'
            }),
            'apellido_materno': forms.TextInput(attrs={
                'class': 'bg-white text-gray-900 rounded-xl pl-2 py-1 md:py-2 text-sm focus:outline-none w-full',
                'placeholder': 'Apellido Materno'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'bg-white text-gray-900 rounded-xl pl-2 py-1 md:py-2 text-sm focus:outline-none w-full',
                'placeholder': 'Ejemplo: Calle 123'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'bg-white text-gray-900 rounded-xl pl-2 py-1 md:py-2 text-sm focus:outline-none w-full',
                'placeholder': 'Ejemplo: 987654321'
            })
        }


#____________________________________________________________________________________________________________________________

# FORMULARIO PARA REGISTRO DE NUEVO USUARIO CREADO POR EL COORDINADOR
class UserCreationForm(forms.ModelForm):
    apellido_paterno = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'bg-white text-gray-900 rounded-xl pl-2 py-1 md:py-2 text-sm focus:outline-none w-full',
            'placeholder': 'Apellido Paterno',
        })
    )
    apellido_materno = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'bg-white text-gray-900 rounded-xl pl-2 py-1 md:py-2 text-sm focus:outline-none w-full',
            'placeholder': 'Apellido Materno',
        })
    )
    rut = forms.CharField(
        max_length=12,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'rut-input bg-white text-gray-900 rounded-xl pl-2 py-1 md:py-2 text-sm focus:outline-none w-full',
            'placeholder': 'Ejemplo: 11111111-1',
            'maxlength': '12',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'bg-white text-gray-900 rounded-xl pl-2 py-1 md:py-2 text-sm focus:outline-none w-full',
                'placeholder': 'Nombre de Usuario',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'bg-white text-gray-900 rounded-xl pl-2 py-1 md:py-2 text-sm focus:outline-none w-full',
                'placeholder': 'Nombres',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'bg-white text-gray-900 rounded-xl pl-2 py-1 md:py-2 text-sm focus:outline-none w-full',
                'placeholder': 'Ejemplo: 7Kqeh@example.com',
            }),
        }

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if Profile.objects.filter(rut=rut).exists():
            raise forms.ValidationError('Este RUT ya existe en el sistema.')
        return rut

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Crear o actualizar el perfil asociado
            profile, created = Profile.objects.get_or_create(user=user)
            profile.apellido_paterno = self.cleaned_data['apellido_paterno'].capitalize()
            profile.apellido_materno = self.cleaned_data['apellido_materno'].capitalize()
            profile.rut = self.cleaned_data['rut']
            profile.save()
        return user