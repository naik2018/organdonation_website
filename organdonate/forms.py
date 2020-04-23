from django.forms import ModelForm
from .models import Donor, Receiver

class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'

class ReceiverForm(ModelForm):
    class Meta:
        model = Receiver
        fields = '__all__'