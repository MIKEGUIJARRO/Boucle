from django.forms import ModelForm
from .models import Cloth

# https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/

class ClothForm(ModelForm):
    class Meta:
        model = Cloth
        fields = '__all__'
        exclude = ['owner']