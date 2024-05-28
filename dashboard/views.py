from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .models import *
from datetime import datetime, time
from .forms import *
from django.contrib import messages


@login_required
def booking(request):
    bookings = Booking.objects.all()
    if request.method == "POST":
        bookform = BookingForm(request.POST)
        if bookform.is_valid():
            bookform.save()
            return redirect("booking")
        else:
            messages.warning(request, bookform.errors)

    else:
        bookform = BookingForm()

    return render(
        request,
        "Booking.html",
        {
            "bookings": bookings,
            "bookform": bookform,
        },
    )


@login_required
def BASE(request):
    return render(request, "base.html")


def admin(request):
    if request.method == "POST":
        userform = SignupForm(request.POST)
        if userform.is_valid():
            userform.save()
            messages.success(request, "Account Added!")
            return redirect("admin")
        else:
            messages.warning(request, userform.errors)

    else:
        userform = SignupForm()

    return render(request, "admin.html", {"userform": userform})


def charts(request):
    return render(request, "Charts.html")


def viewCalendar(request, id=None):
    books = {}
    book = get_object_or_404(Booking, id=id)
    bookform = BookingForm(request.POST, instance=book)
    if bookform.is_valid():
        bookform.save()
        return redirect("view-calendar", id=book.id)
    bookform = BookingForm(instance=book)
    books["bookform"] = bookform
    all_events = Booking.objects.all()
    #### CALENDAR #####
    bookings = []
    customer_book = Booking.objects.filter(id=id)
    for book in customer_book:
        start_date = datetime.combine(book.event_date, book.start_time)
        end_datetime = datetime.combine(book.event_date, book.end_time)

        booking = {
            "title": f"{book.event_type}",
            "start": start_date.isoformat(),
            "end": end_datetime.isoformat(),
        }
        bookings.append(booking)

    return render(
        request,
        "Calendar.html",
        {
            "bookform": bookform,
            "bookings": bookings,
            "all_events": all_events,
        },
    )


def calendar(request):
    all_events = Booking.objects.all()

    return render(
        request,
        "Calendar.html",
        {
            "all_events": all_events,
        },
    )


@login_required
def booking_list(request):
    query = request.GET.get("q")
    if query:
        bookings = Booking.objects.filter(
            Q(client_name__icontains=query)
            | Q(contact_information__icontains=query)
            | Q(event_type__icontains=query)
        )
    else:
        bookings = Booking.objects.all()
    context = {"bookings": bookings, "query": query}
    return render(request, "booking_list.html", context)


@login_required
def booking_form(request, id=None):
    if id:
        booking = get_object_or_404(Booking, pk=id)
    else:
        booking = None

    if request.method == "POST":
        if not booking:
            booking = Booking()

        booking.client_name = request.POST.get("client_name")
        booking.contact_information = request.POST.get("contact_information")
        booking.event_date = request.POST.get("event_date")
        booking.start_time = request.POST.get("start_time")
        booking.end_time = request.POST.get("end_time")
        booking.event_type = request.POST.get("event_type")
        booking.design_service = request.POST.get("design_service") == "Yes"
        booking.number_of_guests = request.POST.get("number_of_guests")
        booking.total_cost = request.POST.get("total_cost")
        booking.downpayment = request.POST.get("downpayment")
        booking.remaining_payment = request.POST.get("remaining_payment")
        booking.payment_status = request.POST.get("payment_status")
        booking.event_status = request.POST.get("event_status")

        booking.save()
        return redirect("booking_list")

    context = {
        "booking": booking,
        "button": "Update" if booking else "Create",
    }
    return render(request, "booking_form.html", context)


@login_required
def delete_booking(request, id=None):
    booking = get_object_or_404(Booking, pk=id)
    booking.delete()
    return redirect("booking_list")


@login_required
def edit_booking(request, id=None):
    return booking_form(request, id)
