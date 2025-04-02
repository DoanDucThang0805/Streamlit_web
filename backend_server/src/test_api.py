import requests
import unittest


BASE_URL = "http://localhost:3001"

class TestMemberAPI(unittest.TestCase):
    def test_add_member(self):
        """Kiểm tra API thêm thành viên"""
        data = {
            "fullname": "Nguyễn Văn A",
            "birthdate": "2000-01-01",
            "hometown": "Hà Nội"
        }
        response = requests.post(f"{BASE_URL}/add_member/", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
    
    def test_search_member_by_name(self):
        """Kiểm tra API tìm kiếm theo tên"""
        search_name = "Nguyễn Văn A"
        response = requests.get(f"{BASE_URL}/search_member/{search_name}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
    
    def test_search_member_by_hometown(self):
        """Kiểm tra API tìm kiếm theo quê quán"""
        search_hometown = "Hà Nội"
        response = requests.get(f"{BASE_URL}/search_hometown/{search_hometown}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
    
    def test_sort_members_by_age(self):
        """Kiểm tra API sắp xếp thành viên theo tuổi"""
        response = requests.get(f"{BASE_URL}/sort_by_age/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

if __name__ == "__main__":
    unittest.main()
