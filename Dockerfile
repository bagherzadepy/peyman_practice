# استفاده از نسخه سبک پایتون
FROM python:3.12-slim

# تعیین دایرکتوری کاری داخل کانتینر
WORKDIR /app

# کپی کردن فایل requirements و نصب وابستگی‌ها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کل پروژه
COPY . .

# دستور پیش‌فرض برای اجرای برنامه
CMD ["python", "src/todo.py"]
