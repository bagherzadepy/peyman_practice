# Todo CLI App (Python)

یک برنامه ساده خط فرمان برای مدیریت تسک ها که داده ها در فایل `tasks.json` ذخیره می شود.

## امکانات و ویژگی ها
- افزودن تسک: `python todo.py add "خرید نان"`
- نمایش تسک ها: `python todo.py list`
- علامت گذاری انجام شده: `python todo.py done 2`
- حذف تسک: `python todo.py remove 2`
- حذف همه: `python todo.py clear`

---

### `requirements.txt`
فعلا نیازی به کتابخانه ی خارجی نداریم

## دستورهای Git محلی
```bash
git add .
git commit -m "Initial commit: Todo CLI App"
```

---

## اجرا
1. پایتون +3.8 نصب کن
2. در پوشه ای که `todo.py` قرار داد از ترمینال فرمان ها را اجرا کن
3. فایل `tasks.json` بعد از اولین افزودن ساخته می شود

## نحوه اجرا
```bash
# اجرای برنامه
python src/todo.py add "خرید نان"
python src/todo.py list
```
## نصب
```bash
python -m venv venv
venv\Scripts\activate       # (روی ویندوز)
source venv/bin/activate    # (روی لینوکس و مک)

pip install -r requirements.txt
```

## گسترش پیشنهادی (ایده ها برای تکمیل پروژه)
- نسخه وب با Flask یا FastAPI
- صفحه مدیریت با فیلتر انجام شده / انجام نشده
- ذخیره سازی با SQLite به جای JSON
- تست های واحد ساده برای تابع ها
