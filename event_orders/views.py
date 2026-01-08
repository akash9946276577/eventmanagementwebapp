from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from events.models import Event
from .models import eventcart, eventbookeditem
from eventusers.models import users  # import your customer model


# ---------------- Existing Cart Views ---------------- #

@login_required
def add_to_cart(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    # ✅ Safely get or create customer profile for the logged-in user
    profile, created = users.objects.get_or_create(user=request.user, defaults={
        'name': request.user.username,
        'email': request.user.email,
        'address': '',
        'phone': ''
    })

    cart, created = eventcart.objects.get_or_create(owner=profile, delete_status=eventcart.LIVE)

    guestcount = int(request.POST.get('guestcount', 1))
    item, created = eventbookeditem.objects.get_or_create(owner=cart, event=event)
    item.guestcount = guestcount
    item.save()

    messages.success(request, f"{event.title} added to your cart.")
    return redirect('orderscart')


@login_required
def show_orderscart(request):
    # ✅ Ensure profile exists
    profile, created = users.objects.get_or_create(user=request.user, defaults={
        'name': request.user.username,
        'email': request.user.email,
        'address': '',
        'phone': ''
    })

    cart = eventcart.objects.filter(owner=profile, delete_status=eventcart.LIVE).first()
    items = cart.added_events.select_related('event').all() if cart else []
    return render(request, 'orderscart.html', {'cart_items': items})


@login_required
def remove_from_cart(request, item_id):
    # ✅ Ensure profile exists
    profile, created = users.objects.get_or_create(user=request.user, defaults={
        'name': request.user.username,
        'email': request.user.email,
        'address': '',
        'phone': ''
    })

    item = get_object_or_404(eventbookeditem, id=item_id, owner__owner=profile)
    item.delete()
    messages.success(request, f"{item.event.title} removed from your cart.")
    return redirect('orderscart')


# ---------------- New Payment Views ---------------- #

@login_required
def payment_page(request):
    """
    Display payment form to the user.
    """
    # ✅ Ensure profile exists
    profile, created = users.objects.get_or_create(user=request.user, defaults={
        'name': request.user.username,
        'email': request.user.email,
        'address': '',
        'phone': ''
    })

    cart = eventcart.objects.filter(owner=profile, delete_status=eventcart.LIVE).first()
    items = cart.added_events.select_related('event').all() if cart else []

    if not items:
        messages.warning(request, "Your cart is empty! Please add events before proceeding to payment.")
        return redirect('orderscart')

    total_amount = 0
    for item in items:
        total_amount += item.event.quote * item.guestcount  # Using quote field from Event model

    context = {
        'cart_items': items,
        'total_amount': total_amount,
    }
    return render(request, 'payment.html', context)


@login_required
def process_payment(request):
    """
    Simulates UPI payment gateway processing.
    You can later integrate Razorpay, Stripe, etc.
    """
    # ✅ Ensure profile exists
    profile, created = users.objects.get_or_create(user=request.user, defaults={
        'name': request.user.username,
        'email': request.user.email,
        'address': '',
        'phone': ''
    })

    if request.method == 'POST':
        cart = eventcart.objects.filter(owner=profile, delete_status=eventcart.LIVE).first()

        if not cart:
            messages.error(request, "No active cart found!")
            return redirect('orderscart')

        # Get payment details from form
        upi_id = request.POST.get('upi_id')
        payment_method = request.POST.get('payment_method')
        
        # Basic UPI ID validation
        if not upi_id or '@' not in upi_id:
            messages.error(request, "Please enter a valid UPI ID!")
            return redirect('payment_page')

        # Simulate payment processing (In real implementation, integrate with payment gateway)
        import time
        time.sleep(1)  # Simulate processing time
        
        # For demo purposes, we'll assume payment is always successful
        # In real implementation, you would:
        # 1. Call payment gateway API
        # 2. Verify payment status
        # 3. Handle success/failure scenarios
        
        payment_successful = True  # This would come from payment gateway response
        
        if payment_successful:
            # Mark cart as completed
            cart.delete_status = eventcart.DELETE  # Mark cart as completed
            cart.event_status = eventcart.EVENT_BOOKED  # Mark as booked
            cart.save()

            # Optionally create a payment record (you can create a Payment model for this)
            # Payment.objects.create(
            #     user=request.user,
            #     cart=cart,
            #     upi_id=upi_id,
            #     payment_method=payment_method,
            #     amount=total_amount,
            #     status='SUCCESS'
            # )

            messages.success(request, f"Payment successful via {payment_method.upper()}! Your events have been booked.")
            return redirect('payment_success')
        else:
            messages.error(request, "Payment failed! Please try again.")
            return redirect('payment_page')

    return redirect('payment_page')


@login_required
def payment_success(request):
    """
    Display a simple payment success page.
    """
    return render(request, 'payment_success.html')
