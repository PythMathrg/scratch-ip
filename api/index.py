from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_ip():
    # Lấy IP của người chơi từ hệ thống Vercel
    user_ip = request.headers.get('x-forwarded-for', request.remote_addr)
    if ',' in user_ip:
        user_ip = user_ip.split(',')[0].strip()
        
    # Loại bỏ dấu chấm để chuyển thành chuỗi số giống như bạn đang làm
    clean_ip = user_ip.replace('.', '')
    
    # Trả trực tiếp chuỗi số này về cho Scratch
    return str(clean_ip)
