from django.conf.urls import url
from BRMapp import views

urlpatterns=[
         url('',views.viewbooks,name='view'),
         url('edit-book',views.editbook,name='edit'),
         url('delete-book',views.deletebook),
         url('search-book',views.searchbook),
         url('new-book',views.newbook),
         url('add',views.add),
         url('search',views.search),
         url('edit',views.edit),
]
