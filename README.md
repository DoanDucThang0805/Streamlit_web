# Streamlit Web

Ứng dụng web dạo lỏ, được xây dựng bằng FastAPI và Streamlit.

## Cài đặt và Chạy

### Cách 1: Sử dụng Docker (Khuyến nghị)

1. Cài đặt Docker và Docker Compose trên máy tính của bạn

2. Clone dự án và di chuyển vào thư mục:
```bash
git clone <repository-url>
cd Streamlit_web
```

3. Mở terminal và chạy lệnh sau:
```bash
docker-compose up --build
```

4. Truy cập ứng dụng:
- Giao diện người dùng: http://localhost:3000
- API: http://localhost:3001

### Cách 2: Chạy trực tiếp trên máy

1. Clone dự án và di chuyển vào thư mục:
```bash
git clone <repository-url>
cd web_em_ngoc_kem
```

#### Cài đặt Backend

1. Mở terminal và di chuyển vào thư mục backend:
```bash
cd backend_server
```

2. Tạo môi trường ảo và kích hoạt:
```bash
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
```

3. Cài đặt thư viện cần thiết:
```bash
pip install -r requirements.txt
```

4. Chạy server:
```bash
uvicorn main:app --reload --port 3001
```

#### Cài đặt Frontend

1. Mở terminal mới và di chuyển vào thư mục frontend:
```bash
cd Frontend
```

2. Tạo môi trường ảo và kích hoạt:
```bash
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
```

3. Cài đặt thư viện cần thiết:
```bash
pip install -r requirements.txt
```

4. Chạy ứng dụng:
```bash
streamlit run app.py
```

## Hướng dẫn Sử dụng

1. Truy cập http://localhost:3000 để sử dụng giao diện người dùng
2. Đăng nhập vào hệ thống
3. Sử dụng các chức năng có sẵn trong menu
