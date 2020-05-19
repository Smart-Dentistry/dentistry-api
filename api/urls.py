from api.medical_records.urls import urlpatterns as medical_records_urls
from api.users.urls import urlpatterns as users_urls


urlpatterns = users_urls + medical_records_urls
