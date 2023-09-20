from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('', view=views.index, name="index"),
    path('', include(tf_urls)),
    path('accounts/register/', view=views.Register.as_view(success_url='/'),
         name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    # insurance staff
    path('insurance_staff/', views.viewClaim, name='insurance_staff'),
    path('insurance_staff_auth/<str:pk>',
         views.authorizeFund, name='insurance_staff_auth'),
    path('insurance_staff_approve/<str:pk>',
         views.approveClaim, name='insurance_staff_approve'),
    path('insurance_staff_reject/<str:pk>',
         views.denyClaim, name='insurance_staff_reject'),
    path('insurance_staff_review/', views.claimDisb,
         name='insurance_staff_review'),

    # lab staff
    path('lab_staff/', views.viewDiagnosis, name='lab_staff'),
    path('lab_staff_approve/<str:diagnosisID>/<str:pk>',
         views.approveTest, name='lab_staff_approve'),
    path('lab_staff_reject/<str:pk>', views.denyTest, name='lab_staff_reject'),
    path('lab_staff_search/', views.lab_search, name='lab_staff_search'),
    path('lab_tests/', views.lab_test_search, name='lab_tests'),
    path('lab_update_record/<str:pk>',views.updateTests, name='lab_update_record'),
    path('lab_delete_record/<str:pk>',views.deleteTest, name='lab_delete_record'),
    path('lab_search_details/<str:pk>',views.diagDetails, name='lab_search_details'),

    # hospital staff
    path('hospital_staff_appointments/', views.hospital_appointment,
         name='hospital_staff_appointments'),
    path('hospital_staff_create_payment/', views.hospital_approved_appointment,
         name='hospital_staff_create_payment'),
    path('hospital_complete_appointment/<str:ID>',
         views.hospital_complete_appointment, name='hospital_complete_appointment'),
    path('hospital_transaction/', views.hospital_transaction,
         name='hospital_transaction'),
    path('hospital_search_patients/', views.hospital_view_patients,
         name='hospital_search_patients'),
    path('hospital_patient_details/',views.hospital_patient_details,name = 'hospital_patient_details'),
    path('hospital_search/',views.hospital_search, name='hospital_search'),
    path('hospital_create_patients/',views.hospital_create_patients,name= 'hospital_create_patients'),
    path('hospital_update_patients/<str:ID>',views.hospital_update_patients,name= 'hospital_update_patients'),
    path('hospital_appointment_approve/<str:ID>',views.hospital_appointment_approve,name='hospital_appointment_approve'),
    path('hospital_appointment_reject/<str:ID>',views.hospital_appointment_reject,name='hospital_appointment_reject'),  
    path('hospital_patient_details/<str:pID>',views.hospital_patient_details,name= 'hospital_patient_details'),
    path('hospital_view_lab_report/<str:testID>',views.hospital_view_lab_report, name='hospital_view_lab_report'),
    path('hospital_test_transaction/<str:testID>',views.hospital_test_transaction, name='hospital_test_transaction'),
    path('hospital_generate_bill',views.hospital_create_bills, name ='hospital_generate_bill'),
    path('hospital_bill/<str:ID>',views.hospital_bill, name = 'hospital_bill'),
    # Patient urls
    path("patient", views.patient, name='patient'),
    path('bot', views.get_bot_response),

    path('patient_details/<str:patientID>',
         views.patient_details, name='patient_details'),
    path('patient_details/update_patient_details/<str:patientID>',
         views.update_patient_record, name='update_patient_details'),

    path("patient_appointment/<str:patientID>",
         views.patient_appointment_view, name="patient_appointment"),
    path('patient_appointment/patient_book_appointment/<str:patientID>',
         views.patient_book_appointment_view, name='patient_book_appointment'),
    path('patient_appointment/patient-view-appointment/<str:patientID>',
         views.patient_previous_appointment_view, name='patient-view-appointment'),

    path('patient_diagnosis/<str:patientID>',
         views.patient_diagnosis_details, name='patient_diagnosis'),
    path('patient_prescription/<str:patientID>',
         views.patient_prescription_details, name='patient_prescription'),

    path("patient_labtest/<str:patientID>",
         views.patient_labtest_view, name="patient_labtest"),
    path("patient_labtest/request_labtest/<str:patientID>",
         views.request_test, name="request_labtest"),
    path("patient_labtest/patient_view_lab_report/<str:patientID>",
         views.view_lab_report, name="patient_view_lab_report"),
    path("patient_view_single_lab_report/<str:testID>",
         views.view_one_lab_report, name="patient_view_single_lab_report"),

    path("patient_payments/<str:patientID>",
         views.patient_payments_details, name="patient_payments"),
    path("patient_make_payment/<str:paymentID>",
         views.make_payment, name="patient_make_payment"),


    # Doctor URLs
    path('doctor/', views.doctor, name='doctor'),
    path('doctor_view_appointment_view/',
         views.doctor_view_appointment_view, name='doctor_appointment'),
    path('doctor_book_appointment/<str:ID>', views.doctor_book_appointment,
         name='doctor_book_appointment'),
    path('doctor_view_patientlist/', views.doctor_view_patientlist,
         name='doctor_view_patientlist'),
#     path('doctor_appointmentID_search_view/', views.doctor_appointmentID_search_view,
#          name='doctor_appointmentID_search_view'),
    path('doctor_search/', views.doctor_search_view,
         name='doctor_search'),
    path('doctor_createpatientdiagnosis_view/<str:ID>', views.doctor_createpatientdiagnosis_view, 
         name='doctor_patient_diagnosis'),
    #path('doctor_view_labreport_view/',
   #      views.doctor_view_labreport_view, name='doctor_view_labreport_view'),
    path('doctor_recommend_labtest/<str:ID>',
         views.doctor_recommend_labtest_view, name='doctor_recommend_labtest_view'),
    path('doctor_create_prescription/<str:ID>', views.doctor_create_prescription_view, 
          name='doctor_create_prescription'),
    path('doctor_update_patients/<str:ID>', views.doctor_update_patients, name='doctor_update_patients'),
    path('doctor_delete_diagnosis/<str:ID>', views.doctor_delete_diagnosis, name='doctor_delete_diagnosis'),
    path('doctor_search_appointment', views.doctor_search_appointment, name='doctor_search_appointment'),
    path('doctor_view_labreport_view/<str:ID>', views.doctor_view_labreport_view, name='doctor_view_labreport_view'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
