from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def get_ip():
    # Lấy IP của người chơi từ hệ thống Vercel
    user_ip = request.headers.get('x-forwarded-for', request.remote_addr)
    if ',' in user_ip:
        user_ip = user_ip.split(',')[0].strip()
        
    # --- THAY ĐỒI Ở ĐÂY ---
    # Thay vì dùng .replace('.', '') để xóa dấu chấm, 
    # tụi mình giữ nguyên biến user_ip ban đầu để có đầy đủ dấu chấm.
    final_ip = str(user_ip)
    
    # Tạo phản hồi trả về chuỗi IP chuẩn (Ví dụ: 42.113.123.45)
    response = make_response(final_ip)
    
    # Giữ nguyên cấu hình CORS để TurboWarp không bị chặn
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    
    return response
