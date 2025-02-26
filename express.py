import requests

username = "giap123"
password = "6VqAC8gyXb3X"

url = "https://demo.wpeverest.com/wp-login.php"

data = {
    "log": username,
    "pwd": password,
    "wp-submit": "Log In",
    "redirect_to": "https://demo.wpeverest.com/wp-admin/user/index.php",
    "testcookie": "1"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://demo.wpeverest.com/wp-login.php",
    "Origin": "https://demo.wpeverest.com"
}

cookies = {
    "wordpress_test_cookie": "WP Cookie check"
}

session = requests.Session()
response = session.post(url, data=data, headers=headers, cookies=cookies)

if "wp-admin" in response.url and response.status_code == 200:
    print("✅ Đăng nhập thành công!")
    print("🔹 Cookie phiên:", session.cookies.get_dict())
else:
    print("❌ Đăng nhập thất bại!")

with open("cookies.txt", "w") as f:
    f.write(str(session.cookies.get_dict()))