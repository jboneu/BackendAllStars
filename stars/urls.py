from .views import give_star_to, star, stars_employee_list
from .views import stars_employee_subcategory_list, stars_employee_subcategory_detail_list, stars_top_employee_lists
from .views import stars_keyword_list
from django.conf.urls import url


urlpatterns = [
    url(r'^(?P<from_employee_id>\d+)/give/star/to/(?P<to_employee_id>\d+)/', give_star_to, name='give_star_to'),
    url(r'^(?P<star_id>\d+)/$', star, name='star_detail'),
    url(r'^(?P<employee_id>\d+)/list/$', stars_employee_list, name='stars_employee_list'),
    url(r'^(?P<employee_id>\d+)/subcategory/list/$', stars_employee_subcategory_list, name='stars_employee_subcategory_list'),
    url(r'^(?P<employee_id>\d+)/subcategory/(?P<subcategory_id>\d+)/list/$',
        stars_employee_subcategory_detail_list,
        name='employee_subcategory_detail_list'),
    url(r'^keyword/list/$', stars_keyword_list, name='stars_keyword_list'),
    url(r'^top/(?P<top_number>\d+)/(?P<kind>\w+)/(?P<id>\d+)/', stars_top_employee_lists, name='stars_top_employee_lists'),
]
