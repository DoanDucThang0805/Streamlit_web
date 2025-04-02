import streamlit as st
import requests
from datetime import datetime

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
        background-color: #FF4B4B;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FF6B6B;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    h1, h2 {
        color: #1E3D59;
        font-weight: bold;
    }
    .success-message {
        padding: 1rem;
        background-color: #D4EDDA;
        border-radius: 5px;
        color: #155724;
    }
    .error-message {
        padding: 1rem;
        background-color: #F8D7DA;
        border-radius: 5px;
        color: #721C24;
    }
    </style>
""", unsafe_allow_html=True)

BASE_URL = "http://backend:3001"

# Sidebar
with st.sidebar:
    st.title("Menu")
    page = st.radio(
        "Chọn chức năng",
        ["Thêm thành viên", "Tìm kiếm", "Sap xep", "Xóa Database"]
    )

# Main content
st.title("Quản lý Thành Viên Nhóm")

if page == "Thêm thành viên":
    st.header("Thêm Thành Viên")
    col1, col2 = st.columns(2)
    
    with col1:
        fullname = st.text_input("Họ và Tên")
        birthdate = st.date_input("Ngày Sinh")
    
    with col2:
        hometown = st.text_input("Quê Quán")
    
    if st.button("Thêm thành viên"):
        with st.spinner("Đang xử lý..."):
            response = requests.post(f"{BASE_URL}/add_member/", json={
                "fullname": fullname,
                "birthdate": str(birthdate),
                "hometown": hometown
            })
            if response.status_code == 200:
                st.markdown(f'<div class="success-message">{response.json()["message"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="error-message">Có lỗi xảy ra: {response.json()["message"]}</div>', unsafe_allow_html=True)

elif page == "Tìm kiếm":
    st.header("Tìm Kiếm Thành Viên")
    search_type = st.radio("Tìm kiếm theo:", ["Tên", "Quê quán"])
    
    if search_type == "Tên":
        search_name = st.text_input("Nhập tên cần tìm")
        if st.button("Tìm"):
            with st.spinner("Đang tìm kiếm..."):
                response = requests.get(f"{BASE_URL}/search_member/{search_name}")
                if response.status_code == 200:
                    data = response.json()
                    if data:
                        st.success(f"Tìm thấy {len(data)} kết quả")
                        for member in data:
                            with st.expander(f"👤 {member['fullname']}"):
                                st.write(f"Ngày sinh: {member['birthdate']}")
                                st.write(f"Quê quán: {member['hometown']}")
                    else:
                        st.warning("Không tìm thấy thành viên nào")
                else:
                    st.error("Có lỗi xảy ra khi tìm kiếm")
    
    else:
        search_hometown = st.text_input("Nhập quê quán cần tìm")
        if st.button("Tìm"):
            with st.spinner("Đang tìm kiếm..."):
                response = requests.get(f"{BASE_URL}/search_hometown/{search_hometown}")
                if response.status_code == 200:
                    data = response.json()
                    if data:
                        st.success(f"Tìm thấy {len(data)} kết quả")
                        for member in data:
                            with st.expander(f"👤 {member['fullname']}"):
                                st.write(f"Ngày sinh: {member['birthdate']}")
                                st.write(f"Quê quán: {member['hometown']}")
                    else:
                        st.warning("Không tìm thấy thành viên nào")
                else:
                    st.error("Có lỗi xảy ra khi tìm kiếm")

elif page == "Xóa Database":
    st.header("Xóa Database")
    st.warning("⚠️ CẢNH BÁO: Hành động này sẽ xóa tất cả dữ liệu trong database!")
    
    # Yêu cầu xác nhận từ người dùng
    confirm = st.text_input("Nhập 'XÓA' để xác nhận xóa database:")
    
    if st.button("Xóa Database"):
        if confirm == "XÓA":
            with st.spinner("Đang xóa database..."):
                response = requests.delete(f"{BASE_URL}/reset_database/")
                if response.status_code == 200:
                    st.markdown(f'<div class="success-message">{response.json()["message"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="error-message">Có lỗi xảy ra: {response.json()["message"]}</div>', unsafe_allow_html=True)
        else:
            st.error("Vui lòng nhập 'XÓA' để xác nhận")

else:
    st.header("Danh sách thành viên theo tuổi")
    if st.button("Sắp xếp theo tuổi"):
        with st.spinner("Đang xử lý..."):
            response = requests.get(f"{BASE_URL}/sort_by_age/")
            if response.status_code == 200:
                data = response.json()
                if data:
                    st.success(f"Tổng số thành viên: {len(data)}")
                    
                    # Chuyển đổi dữ liệu để hiển thị trong bảng
                    table_data = []
                    for member in data:
                        table_data.append({
                            "Họ và Tên": member['fullname'],
                            "Ngày Sinh": member['birthdate'],
                            "Quê Quán": member['hometown']
                        })
                    
                    # Hiển thị bảng với định dạng
                    st.dataframe(
                        table_data,
                        column_config={
                            "Họ và Tên": st.column_config.TextColumn("Họ và Tên", width="medium"),
                            "Ngày Sinh": st.column_config.TextColumn("Ngày Sinh", width="small"),
                            "Quê Quán": st.column_config.TextColumn("Quê Quán", width="medium")
                        },
                        hide_index=True,
                    )
                else:
                    st.warning("Không có thành viên nào")
            else:
                st.error("Có lỗi xảy ra khi lấy danh sách")
