
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
  
]
admin.site.site_header= "Sir Felix Portfolio Administration"
admin.site.site_title="Portfolio"
admin.site.index_title="Welcome to Sir Felix Portfolio Administration"
