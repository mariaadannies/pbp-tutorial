from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_wishlist_xml
from wishlist.views import show_wishlist_json
from wishlist.views import show_wishlist_json_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('wishlist_xml/', show_wishlist_xml, name='show_wishlist_xml'),
    path('wishlist_json/', show_wishlist_json, name='show_wishlist_json'),
    path('wishlist_json_id/<int:id>', show_wishlist_json_id, name='show_wishlist_json_id')
]