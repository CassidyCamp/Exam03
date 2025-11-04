## **File Handling – TXT fayl**

### ✅ **1. Foydalanuvchi ma’lumotini yozish**

📄 `data.txt` fayliga foydalanuvchi ismi va yoshini yozing.

**Shartlar:**

* Foydalanuvchidan `input()` orqali ism va yosh so‘raladi.
* Har bir foydalanuvchi yangi qatorda yozilsin (`a` rejimi).
* Format: `Ali – 15 yosh`

---

### ✅ **2. TXT fayldan o‘qish**

📄 `data.txt` faylini o‘qib, barcha foydalanuvchi ma’lumotlarini ekranga chiqaring.

**Shartlar:**

* `with open(..., "r")` dan foydalaning.
* Har bir qatorni `strip()` bilan tozalang.
* Fayl mavjud bo‘lmasa, `"Fayl topilmadi!"` xabarini chiqaring (`try/except` bilan).

---

### ✅ **3. TXT fayldagi qatorlar sonini hisoblash**

📄 `data.txt` faylida nechta foydalanuvchi ma’lumotlari yozilganini hisoblang.

**Shartlar:**

* Fayl mavjudligini `try/except` bilan tekshiring.
* Fayl ochilsa, `len(readlines())` bilan qatorlar sonini aniqlang.
* Natijani ekranga chiqarish:
  `data.txt faylida 5 ta foydalanuvchi mavjud`

---

## **File Handling – JSON fayl**

### ✅ **4. JSON faylga ma’lumot yozish**

📦 `data.json` faylini yarating va foydalanuvchi ma’lumotlarini yozing.

**Shartlar:**

* Foydalanuvchidan ism va yosh so‘raladi.
* Faylga quyidagi formatda yozilsin:

```json
{"name": "Ali", "age": 15}
```

* Har safar yangi foydalanuvchi qo‘shilganda, faylni yangilang (append emas, ro‘yxatga qo‘shib).
* Fayl bo‘sh bo‘lsa, bo‘sh ro‘yxat yarating.

---

### ✅ **5. JSON fayldan o‘qish**

📦 `data.json` faylini o‘qib, barcha foydalanuvchi ma’lumotlarini ekranga chiqaring.

**Shartlar:**

* `json.load()` dan foydalaning.
* Har bir foydalanuvchi uchun:
  `Name: Ali, Age: 15`
* Fayl mavjud bo‘lmasa, `"Fayl topilmadi!"` xabarini chiqaring.

---

### ✅ **6. JSON faylda ma’lumot qo‘shish**

📦 `data.json` fayliga yangi foydalanuvchi qo‘shing.

**Shartlar:**

* Avval fayldan barcha ma’lumotlarni o‘qing (`json.load()`).
* Yangi foydalanuvchi obyektini ro‘yxatga qo‘shing.
* Faylni yangilab saqlang (`json.dump()`).
* Natija ekranga chiqsin:
  `Foydalanuvchi JSON faylga qo‘shildi!`

---

## **Python OOP**

### ✅ **7. Book klassini yozing**

📚 `Book` nomli klass yozing.

**Atributlar:**

* `title`, `author`, `year`

**Shartlar:**

* `__init__()` konstruktor orqali qiymatlarni qabul qilsin.
* 2 ta book obyektini yaratib, ma’lumotlarini `print()` bilan chiqaring.

---

### ✅ **8. Rectangle klassi – To‘rtburchak yuzasi**

⬛ `Rectangle` klassi:

**Atributlar:** `width`, `height`
**Metod:** `area()` – yuzani hisoblaydi (`width * height`)

**Shartlar:**

* 2 ta obyekt sinab ko‘ring va yuzalarni chiqarish.

---

### ✅ **9. Animal klassi – Hayvon tovushi**

🐾 `Animal` klassi:

**Atributlar:** `name`, `sound`
**Metod:** `make_sound()` → `"Dog says Woof!"`

**Shartlar:**

* 2 ta hayvon obyektini yaratib, metodni chaqiring.

---

### ✅ **10. BankAccount klassi – Hisob bilan ishlash**

🏦 `BankAccount` klassi:

**Atributlar:** `owner`, `balance`
**Metodlar:** `deposit(amount)`, `withdraw(amount)` (balans yetarli bo‘lmasa `"Balans yetarli emas"`)

---

### ✅ **11. Inheritance – Vehicle va Car**

🚗 `Vehicle` klassi: `brand`, `model`, `move()` → `"Vehicle is moving"`
`Car` klassi (`Vehicle` dan meros oladi): `move()` → `"Car is driving"`

**Shartlar:**

* Har ikkala klassdan obyekt yarating va `move()` metodini sinab ko‘ring.

---

### ✅ **12. Inheritance – Person va Student**

👨‍🎓 `Person` klassi: `name`, `age`, `introduce()`
`Student` klassi: qo‘shimcha `grade`, `introduce()` metodini qayta yozish

**Shartlar:**

* Har ikkala klassdan obyekt yaratib, metodlarni sinab ko‘ring.

---

### ✅ **13. Polymorphism – Shape**

🟢 Bazaviy `Shape` klassi, `area()` metod bo‘sh (pass)
`Rectangle` va `Circle` undan meros oladi

**Shartlar:**

* `Rectangle`: `area()` → `width * height`
* `Circle`: `area()` → `3.14 * radius ** 2`
* Obyektlarni ro‘yxatga joylab, sikl orqali yuzalarni chiqarish.

---

### ✅ **14. Calculator klassi – Try/Except bilan**

🧮 `Calculator` klassi: `divide(a, b)` metod

**Shartlar:**

* Agar `b=0` bo‘lsa, `"Bo‘lishda xatolik"` xabarini chiqaring (`try/except` bilan).

---

### ✅ **15. Oddiy Class

**Vazifa:** `Phone` nomli class yarating. Uning `brand`, `model` atributlari bo'lsin va `show_info()` metodi telefon haqida ma'lumot chiqarsin.

**Misol:**
```python
phone = Phone("Samsung", "Galaxy S21")
phone.show_info()
```

**Natija:**
```
Phone: Samsung Galaxy S21
```

### ✅ **16. Polymorphism – Bird va Dog**

🐦 `Bird` va 🐕 `Dog` klasslari, har biri `speak()` metodiga ega

**Shartlar:**

* Ro‘yxatga joylab, sikl orqali `speak()` chaqirish

---

### ✅ **17. Full Project – User Manager**

👥 `User` klassi:

**Atributlar:** `username`, `email`, `is_active`
**Metodlar:** `save()`, `deactivate()`

**Shartlar:**

* 2 ta foydalanuvchi yaratish: biri faol (`True`), biri nofaol (`False`)
* Faylga yozing va fayldan o‘qib ma’lumotni chiqarish

---
