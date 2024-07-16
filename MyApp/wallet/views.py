from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from user.models import Profile
from .models import PaymentForm, ComboPoint, PaymentHistory
from .vnpay import vnpay

point = _order_id = _amount = _order_desc = combo_point_id = None

@login_required(login_url='user/login/')
def view_buy_point(request):
    global point, _order_id, _amount, _order_desc, combo_point_id
    return_code = request.GET.get('vnp_ResponseCode')
    print(f'return_code: {return_code}')
    if return_code == '00':
        _profile = get_object_or_404(Profile, user=request.user)
        _profile.point += point
        _profile.save()
        _combo_point = get_object_or_404(ComboPoint, id=combo_point_id)
        PaymentHistory.objects.create(
            user=request.user,
            combo_point = _combo_point,
            order_id = _order_id,
            amount = _amount,
            order_desc = _order_desc,
            order_date = timezone.now(),
        )
    combo_point = ComboPoint.objects.all()
    return render(request, 'wallet/buy_point.html', {'combo_point' : combo_point})

@login_required(login_url='user/login/')
def payment(request):
    global point, _order_id, _amount, _order_desc, combo_point_id
    if request.method == 'POST':
        # Process input data and build url payment
        form = PaymentForm(request.POST)
        if form.is_valid():
            _order_id = form.cleaned_data['order_id']
            _amount = form.cleaned_data['amount']
            _order_desc = form.cleaned_data['order_desc']
            bank_code = ""
            language = form.cleaned_data['language']
            point = form.cleaned_data['point']
            combo_point_id = form.cleaned_data['combo_point']
            ipaddr = get_client_ip(request)
            # Build URL Payment
            vnp = vnpay()
            vnp.requestData['vnp_Version'] = '2.1.0'
            vnp.requestData['vnp_Command'] = 'pay'
            vnp.requestData['vnp_TmnCode'] = settings.VNPAY_TMN_CODE
            vnp.requestData['vnp_Amount'] = _amount * 100
            vnp.requestData['vnp_CurrCode'] = 'VND'
            vnp.requestData['vnp_TxnRef'] = _order_id
            vnp.requestData['vnp_OrderInfo'] = _order_desc
            vnp.requestData['vnp_OrderType'] = 'billpayment'
            # Check language, default: vn
            if language and language != '':
                vnp.requestData['vnp_Locale'] = language
            else:
                vnp.requestData['vnp_Locale'] = 'vn'
                # Check bank_code, if bank_code is empty, customer will be selected bank on VNPAY
            if bank_code and bank_code != "":
                vnp.requestData['vnp_BankCode'] = bank_code
            vnp.requestData['vnp_CreateDate'] = datetime.now().strftime('%Y%m%d%H%M%S')
            vnp.requestData['vnp_IpAddr'] = ipaddr
            vnp.requestData['vnp_ReturnUrl'] = settings.VNPAY_RETURN_URL
            vnpay_payment_url = vnp.get_payment_url(settings.VNPAY_PAYMENT_URL, settings.VNPAY_HASH_SECRET_KEY)
            print(vnpay_payment_url)
            return redirect(vnpay_payment_url)
        else:
            print("Form input not validate")
            combo_point = ComboPoint.objects.all()
            return render(request, 'wallet/buy_point.html', {'combo_point' : combo_point})
    else:
        return_code = request.GET.get('vnp_ResponseCode')
        print(f'return_code: {return_code}')
        if return_code == '00':
            _profile = get_object_or_404(Profile, user=request.user)
            _profile.point += point
            _profile.save()
            _combo_point = get_object_or_404(ComboPoint, id=combo_point_id)
            PaymentHistory.objects.create(
                user=request.user,
                combo_point = _combo_point,
                order_id = _order_id,
                amount = _amount,
                order_desc = _order_desc,
                order_date = timezone.now(),
            )
        combo_point = ComboPoint.objects.all()
        return render(request, 'wallet/buy_point.html', {'combo_point' : combo_point})

@login_required(login_url='user/login/')
def payment_history(request):
    history = PaymentHistory.objects.filter(user=request.user)
    return render(request, 'wallet/history.html', {'history' : history})

@login_required(login_url='user/login/')
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip