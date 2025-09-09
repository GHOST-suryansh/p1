from django.shortcuts import render
import qrcode
from io import BytesIO
import base64

def qr(request):
    qr_image = None   # latest QR only
    text = ''         # input field value

    if request.method == 'POST':
        # Clear All QR Codes logic (ab waise bhi ek hi QR hai, fir bhi future proof)
        if 'clear' in request.POST:
            qr_image = None
            text = ''
        else:
            text = request.POST.get('text', '')
            if text:
                qr_code = qrcode.QRCode(version=1, box_size=10, border=5)
                qr_code.add_data(text)
                qr_code.make(fit=True)
                img = qr_code.make_image(fill='black', back_color='white')
                buffer = BytesIO()
                img.save(buffer, format='PNG')
                qr_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render(request, 'qr/qr.html', {
        'qr_image': qr_image,
        'text': '',
    })
