# Todo CLI App (Python)

یک برنامه ساده خط فرمان برای مدیریت تسک ها که داده ها در فایل `tasks.json` ذخیره می شود.

## امکانات و ویژگی ها
- افزودن تسک: `python todo.py add "خرید نان"`
- نمایش تسک ها: `python todo.py list`
- علامت گذاری انجام شده: `python todo.py done 2`
- حذف تسک: `python todo.py remove 2`
- حذف همه: `python todo.py clear`

---

## 📦 ساختار پروژه
peyman_practice/
│── src/
│ └── todo.py
│── tests/
│ └── test_todo.py
│── docs/
│ └── intro.md
│── .flake8
│── .gitignore
│── .pre-commit-config.yaml
│── requirements.txt
│── Dockerfile
│── README.md
│── LICENSE
│── CONTRIBUTING.md

---

### `requirements.txt`
فعلا نیازی به کتابخانه ی خارجی نداریم

## دستورهای Git محلی
```bash
git add .
git commit -m "Initial commit: Todo CLI App"
```

---

## ⚡ نصب و اجرا
```bash
git clone https://github.com/bagherzadepy/peyman_practice.git
cd peyman_practice
python -m venv venv
source venv/bin/activate  # یا در ویندوز: venv\Scripts\activate
pip install -r requirements.txt
```

## اجرا
1. پایتون +3.8 نصب کن
2. در پوشه ای که `todo.py` قرار داد از ترمینال فرمان ها را اجرا کن
3. فایل `tasks.json` بعد از اولین افزودن ساخته می شود

## ✅ اجرای برنامه
```bash
# اجرای برنامه
python src/todo.py add "خرید نان"
python src/todo.py list
```

---

🧪 اجرای تست‌ها
```bash
pytest
```

🐳 اجرای Docker
```bash
docker build -t peyman_practice .
docker run --rm peyman_practice
```

---

## گسترش پیشنهادی (ایده ها برای تکمیل پروژه)
- نسخه وب با Flask یا FastAPI
- صفحه مدیریت با فیلتر انجام شده / انجام نشده
- ذخیره سازی با SQLite به جای JSON
- تست های واحد ساده برای تابع ها

---

📄 مجوز
این پروژه تحت لایسنس MIT منتشر شده است.
