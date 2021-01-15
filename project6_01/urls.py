from django.urls import path
from project6_01.views import index_page
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index_page/',index_page)
]