# Sử dụng Python 3.10 slim làm base image
FROM python:3.10-slim

# Đặt thư mục làm việc trong container
WORKDIR /frontend

# Sao chép file requirements.txt vào container
COPY requirements.txt .

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn frontend vào container
COPY src/ .

# Expose cổng (tùy thuộc vào framework bạn dùng)
EXPOSE 3000

# Chạy ứng dụng (tùy vào cách bạn khởi chạy frontend)
CMD ["streamlit", "run", "app.py", "--server.port=3000", "--server.address=0.0.0.0"]
