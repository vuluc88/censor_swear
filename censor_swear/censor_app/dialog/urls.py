from django.urls import path
from .project_views import *
from .project_import_views import *

urlpatterns = [
    path('<int:project_id>/upload-raw-masking-data', UploadRawMaskingDataView.as_view()),
    path('<int:project_id>/masking/system_verify_count', get_masking_csv_system_verify_count),
    path('<int:project_id>/masking/manual_verify_count', get_masking_csv_manually_verify_count),
]
