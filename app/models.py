from django.db import models


class Doctor(models.Model):
    doctorID = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField()
    value = models.BigIntegerField()


class Patient(models.Model):
    patientID = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=128,null=True)
    height = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    weight = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    insuranceID = models.IntegerField(blank=True, null=True)


class Appointment(models.Model):
    appointmentID = models.BigAutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    type = models.CharField(max_length=255)
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    doctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    diagnosisID = models.ForeignKey(
        'Diagnosis', on_delete=models.CASCADE, blank=True, null=True)
    testID = models.ForeignKey('Test', on_delete=models.CASCADE, blank=True, null=True)
    paymentID = models.ForeignKey(
        'Payment', on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    paymentID = models.BigAutoField(primary_key=True)
    method = models.CharField(max_length=255)
    amount = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255)
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE,blank=True, null=True)
    testID = models.ForeignKey('Test', on_delete=models.CASCADE,blank=True, null=True)
    appointmentID = models.ForeignKey(Appointment, on_delete=models.CASCADE,blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Insurance(models.Model):
    request_id = models.AutoField(primary_key=True)
    paymentID = models.ForeignKey(Payment, on_delete=models.CASCADE)
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)


class Diagnosis(models.Model):
    diagnosisID = models.BigAutoField(unique=True, primary_key=True)
    doctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointmentID = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=256)
    test_recommendation = models.CharField(max_length=256)
    prescription = models.CharField(max_length=256, blank=True, null=True)


class Test(models.Model):
    testID = models.BigAutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    type = models.CharField(max_length=255)
    patientID = models.ForeignKey(Patient, blank=True, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, blank=True, null=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    diagnosisID = models.ForeignKey(Diagnosis,blank=True, null = True, on_delete=models.CASCADE)
    paymentID = models.ForeignKey(Payment, blank=True, null = True, on_delete=models.CASCADE)
