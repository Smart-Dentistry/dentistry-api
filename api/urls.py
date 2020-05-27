from api.medical_records.urls import urlpatterns as medical_records_urls
from api.users.urls import urlpatterns as users_urls
from api.s3.urls import urlpatterns as s3_urls


urlpatterns = users_urls + medical_records_urls + s3_urls
