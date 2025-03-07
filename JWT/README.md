### Lab 1: JWT authentication bypass via unverified signature
- Sau khi login với tài khoản `wiener:peter`, JWT token được lưu trong Cookies session. 

    ![alt text](/JWT/image/image-11.png)

- Xem nó bằng jwt.io

    ![alt text](/JWT/image/image-12.png)

- Thử bypass bằng cách sửa đổi phần `signature=False` và set tên người dùng thành `administrator`. Code bypass [JWT_lab_1](JWT_lab_1.py)

    ![alt text](/JWT/image/image-13.png)

- Cầm token mới và dán vào web. Kết quả cho thấy đã bypass login thành `admin`

    ![alt text](/JWT/image/image-14.png)

- Xóa người dùng `carlos` là solve thành công bài này!

    ![alt text](/JWT/image/image-15.png)

### Lab 2: JWT authentication bypass via flawed signature verification
- Tương tự như bài 1, thử xem JWT sau khi đăng nhập

    ![alt text](/JWT/image/image-16.png)

- Bypass bài này thay đổi phần `alg` thành `None`. Code bypass [JWT_lab_2](JWT_lab_2.py)

    ![alt text](/JWT/image/image-17.png)

    - Điều này tương đương với hoàn toàn bỏ qua phần `signature`

    ![alt text](/JWT/image/image-18.png)

- Cầm token mới dán vào web là đã trở thành `admin`

    ![alt text](/JWT/image/image-19.png)

- Xóa carlos là solve bài này

    ![alt text](/JWT/image/image-20.png)

### Lab 3: JWT authentication bypass via weak signing key
- JWT gốc

    ![alt text](/JWT/image/image-8.png)
    - Bài này khai thác việc sử dụng khóa bí mật yếu, dễ bị bruteforce

- Code bruteforce secret key [JWT_lab_3](JWT_lab_3.py), với wordlist được dùng là [jwt secrets list](jwt.secrets.list)

    ![alt text](/JWT/image/image-21.png)

    - Valid key tìm được là `secret1`

- Dán secret key tìm được vào và xác thực signature

    ![alt text](/JWT/image/image-22.png)


- Sửa đổi lại tên người dùng thành `administrator`, dán token mới vào web là đã thành `admin`

    ![alt text](/JWT/image/image-23.png)

    ![alt text](/JWT/image/image-24.png)

- Xóa carlos là solve bài này

    ![alt text](/JWT/image/image-25.png)