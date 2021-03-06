from django.conf.urls import url
from .views import (
                    home_page, 
                    sql, formparameter, 
                    header, 
                    xss, 
                    documentation,
                    feedback,
                    )

app_name = 'dbdex'

urlpatterns = [
    url(r'^$', home_page, name ="home" ),
    url(r'^sql/$', sql, name="sql" ),
    url(r'^formparameter/$', formparameter, name="formparameter" ),
    url(r'^header/$', header, name="header" ),
    url(r'^xss/$', xss, name="xss" ),
    url(r'^documentation/$', documentation, name='doc'),
    url(r'^feedback/$', feedback, name='feedback'),
]
