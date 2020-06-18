from django.urls import path
from .views import post_list_view, post_detail_view, mail_send_view
urlpatterns = [
    path('', post_list_view),
    path('tag/<slug:tag_slug>', post_list_view, name="post_list_by_tag_name"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail_view, name='post_detail'),
    path('<int:id>/share', mail_send_view)
]
