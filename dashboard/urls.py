from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(views.BASE), name="BASE"),
    path("Admin/", views.admin, name="admin"),
    path("Booking/", views.booking, name="booking"),
    path("Charts/", views.charts, name="charts"),
    path("calendar/", views.calendar, name="calendar"),
    path("view-calendar/<int:id>/", views.viewCalendar, name="view-calendar"),
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/add/', views.booking_form, name='booking_form'),
    path('bookings/edit/<int:id>/', views.edit_booking, name='edit_booking'),
    path('bookings/delete/<int:id>/', views.delete_booking, name='delete_booking'),


]
