from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import include, path
from . import views

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('bookings', views.bookings, name='bookings'),

    # Function based API Views
    path('menu_api_view/', views.MenuItemsView.as_view()),
    path('menu_api_view/<int:pk>', views.SingleMenuItemView.as_view()),

    # Class-Based API views using the router
    path('booking/', include(router.urls)),

    # API Token authentication
    path('api-token-auth/', obtain_auth_token)
]




