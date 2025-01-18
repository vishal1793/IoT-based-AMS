import logging
import requests
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import JsonResponse
from .models import Asset_table, Kit_table, Kit_table2, NewTable  # Import NewTable model
import datetime
from django.views.decorators.csrf import csrf_exempt
from app.forms import UIDForm
from django.db import IntegrityError
import pytz
from django.utils import timezone

# Get logger instance
logger = logging.getLogger(__name__)

@csrf_exempt
def save_rfid_data(request):
    if request.method == 'POST':
        # Extract the sum_value from the request data
        sum_value = request.POST.get('sum_value')
        if sum_value:
            # Create an instance of the NewTable model with the sum_value
            new_data = NewTable(sum_value=sum_value)
            new_data.save()
            return JsonResponse({'message': 'Data saved successfully'})
        else:
            return JsonResponse({'error': 'sum_value parameter is missing'}, status=400)
    else:
        # Reject GET requests
        return JsonResponse({'error': 'GET request received, but this endpoint is for POST requests only'}, status=405)

# Function to send POST request
def send_post_request():
    url = 'http://192.168.29.196:8000/save-rfid-data/'  # Change URL to your server's URL
    sum_value = 42  # Change sum value to whatever you want to send
    data = {'sum_value': sum_value}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            logger.info('POST request successful')
        else:
            logger.error('POST request failed with status code: %d', response.status_code)
    except Exception as e:
        logger.error('Error occurred while sending POST request: %s', str(e))

# Call the function to send the POST request
send_post_request()

def home(req):
    return render(req,'index.html')

def reg(req):
    # Fetch the latest sum_value from NewTable
    latest_sum_value = NewTable.objects.last().sum_value if NewTable.objects.exists() else None
    
    if latest_sum_value:
        kit_id = req.POST.get('kitid')
        loc_place = req.POST.get('loc')
        context = {
            'kitid': kit_id,
            'l_p': loc_place,
            'uid': latest_sum_value
        }
        return render(req, 'UID.html', context)
    else:
        # Handle the case where no sum_value is available
        # Redirect to an error page or display a message
        return HttpResponse("Error: No UID available")

def UID(request):
    if request.method == 'POST':
        form = UIDForm(request.POST)
        if form.is_valid():
            kit_id = form.cleaned_data['kitid']
            loc_place = form.cleaned_data['loc']
            uid = form.cleaned_data['uid']
            return render(request, 'confirm.html', {'kitid': kit_id, 'loc': loc_place, 'uid': uid})
    else:
        form = UIDForm()
    return render(request, 'UID.html', {'form': form})

def inloc(req):
    try:
        if req.method == 'POST':
            kitid = req.POST.get('kitid')
            loc_place = req.POST.get('loc')
            uid = req.POST.get('uid')
            asset_instance = get_object_or_404(Asset_table, uid=uid)
            existing_entry = Kit_table.objects.filter(uid=asset_instance)
            if existing_entry.exists():
                if existing_entry.first().kit_id != kitid:
                    existing_entry.delete()
                    # Localize time to Indian timezone
                    in_loc_ts = timezone.now().astimezone(pytz.timezone('Asia/Kolkata'))
                    Kit_table.objects.create(kit_id=kitid, in_loc_place=loc_place, uid=asset_instance, in_loc_ts=in_loc_ts)
                    return HttpResponse("success")
                else:
                    return HttpResponse("Kit ID already exists for this UID")
            else:
                # Localize time to Indian timezone
                in_loc_ts = timezone.now().astimezone(pytz.timezone('Asia/Kolkata'))
                Kit_table.objects.create(kit_id=kitid, in_loc_place=loc_place, uid=asset_instance, in_loc_ts=in_loc_ts)
                return HttpResponse("success")
    except IntegrityError as e:
        return HttpResponse("IntegrityError: " + str(e))
    return HttpResponse("error")

def outloc(req):
    try:
        if req.method == 'POST':
            kitid = req.POST.get('kitid')
            loc_place = req.POST.get('loc')
            uid = req.POST.get('uid')
            asset_instance = get_object_or_404(Asset_table, uid=uid)
            existing_entry = Kit_table2.objects.filter(uid=asset_instance)
            if existing_entry.exists():
                if existing_entry.first().kit_id != kitid:
                    existing_entry.delete()
                    # Localize time to Indian timezone
                    out_loc_ts = timezone.now().astimezone(pytz.timezone('Asia/Kolkata'))
                    Kit_table2.objects.create(kit_id=kitid, out_loc_place=loc_place, uid=asset_instance, out_loc_ts=out_loc_ts)
                    return HttpResponse("success")
                else:
                    return HttpResponse("Kit ID already exists for this UID")
            else:
                # Localize time to Indian timezone
                out_loc_ts = timezone.now().astimezone(pytz.timezone('Asia/Kolkata'))
                Kit_table2.objects.create(kit_id=kitid, out_loc_place=loc_place, uid=asset_instance, out_loc_ts=out_loc_ts)
                return HttpResponse("success")
    except IntegrityError as e:
        return HttpResponse("IntegrityError: " + str(e))
    return HttpResponse("error")
