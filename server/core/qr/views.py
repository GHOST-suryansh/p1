
from django.shortcuts import render
import qrcode
from io import BytesIO
import base64

def qr(request):
    qr_image = None
    text = ''
    if request.method == 'POST':
        text = request.POST.get('text', '')
        if text:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            qr_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return render(request, 'qr/qr.html', {'qr_image': qr_image, 'text': text})
