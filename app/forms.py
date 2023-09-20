from django import forms
from django.utils.translation import gettext_lazy as _
from two_factor.utils import totp_digits

from . import models


class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = ['name', 'age', 'gender', 'height', 'weight', 'insuranceID']


class PatientAppointmentForm(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields = ['date', 'time', 'doctorID']


class RequestLabTestForm(forms.ModelForm):
    otp_token = forms.IntegerField(label=_("Token"), min_value=1,
                                   max_value=int('9' * totp_digits()))
    def __init__(self, *args, **kwargs):
        self.patientID = kwargs.pop('patientID')
        super(RequestLabTestForm, self).__init__(*args, **kwargs)
        self.fields['diagnosisID'] = forms.ModelChoiceField(
            queryset=models.Diagnosis.objects.filter(patientID=self.patientID))

    class Meta:
        model = models.Test
        fields = ['type', 'date', 'time', 'diagnosisID', 'otp_token']


class MakePaymentForm(forms.ModelForm):
    otp_token = forms.IntegerField(label=_("Token"), min_value=1,
                                   max_value=int('9' * totp_digits()))
    class Meta:
        model = models.Payment
        fields = ['method', 'otp_token']


class PatientUpdateForm(forms.Form):
    PatientName = forms.CharField(
        label='Patient Name', max_length=100)
    Age = forms.CharField(label='Age', max_length=100, required=False)
    Gender = forms.CharField(label='Gender', max_length=50, required=False)
    Height = forms.CharField(label='Height', required=False)
    Weight = forms.CharField(label='Weight', required=False)
    InsuranceID = forms.CharField(
        label='Insurance ID', max_length=10, required=False)


class CreatePaymentForm(forms.Form):
    Amount = forms.CharField(label='Amount', max_length=50)


class EditDiagnosisForm(forms.ModelForm):
    class Meta:
        model = models.Diagnosis
        fields = ['diagnosis']


class RecommendLabTest(forms.ModelForm):
    class Meta:
        model = models.Diagnosis
        fields = ['test_recommendation']


class CreatePrescription(forms.ModelForm):
    class Meta:
        model = models.Diagnosis
        fields = ['prescription']


class EditReportForm(forms.ModelForm):
    class Meta:
        model = models.Test
        fields = ['result']


class DoctorAppointmentForm(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields = ['date', 'time','diagnosisID','type']
