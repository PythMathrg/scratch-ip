from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def get_ip():
    # Lấy IP của người chơi từ hệ thống Vercel
    user_ip = request.headers.get('x-forwarded-for', request.remote_addr)
    if ',' in user_ip:
        user_ip = user_ip.split(',')[0].strip()
        
    clean_ip = user_ip.replace('.', '')
    
    # Tạo phản hồi trả về chuỗi số IP
    response = make_response(str(clean_ip))
    
    # BẬT CÔNG TẮC CORS: Cho phép tất cả các trang web (bao gồm TurboWarp) đọc được dữ liệu này
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    
    return response
