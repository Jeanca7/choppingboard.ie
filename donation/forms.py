from django import forms
from .models import Donor

class MakeDonationForm(forms.Form):
    #add donation input here
    MONTH_CHOICES = [(i, i,) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i,) for i in range(2018, 2040)]

    donation_quantity = forms.DecimalField(max_digits=6, decimal_places=2)
    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'