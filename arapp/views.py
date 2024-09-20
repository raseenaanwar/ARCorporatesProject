from django.shortcuts import render

def home(request):
    return render(request,'index.html')

from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        message_content = request.POST.get('message')

        subject = f"New Message from {name} regarding {service}"
        message = f"Name: {name}\nEmail: {email}\nService: {service}\nMessage: {message_content}"

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['arcorpenquiriesar@gmail.com'],
                fail_silently=False,
            )
            # Return a JSON response to be handled by your AJAX call
            return JsonResponse({'success': True, 'name': name})
        except Exception as e:
            # Handle error and return JSON with error message
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    # If not a POST request, return a bad request response
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)
