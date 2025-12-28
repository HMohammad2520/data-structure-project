<div align="right" dir="rtl">

# (Data Structures with C++)

## پروژه ساختمان داده‌ها

---

## مقدمه

این پروژه شامل پیاده‌سازی درس‌های مختلف ساختمان داده‌ها در زبان **C++** است.
هدف پروژه آموزش و تمرین مفاهیم پایه مانند **پشته، صف، لیست پیوندی، عبارات پسوندی و پیشوندی، بازگشت، و کاربردهای آنها** می‌باشد.
همچنین، پروژه به گونه‌ای طراحی شده که بتوانید با استفاده از فایل‌های **Compile** و **Test** عملیات کامپایل و اجرای برنامه‌ها را به صورت خودکار انجام دهید.

---

## فهرست دروس

| Lesson                | Chapter Readme                                         | C++ File                                              |
| --------------------- | ------------------------------------------------------ | ----------------------------------------------------- |
|                       | **— [Chapter 1](source/chapter_1/) —**                 |                                                       |
| Factorial             | [Readme](source/chapter_1/01_factorial.md)             | [Code](source/chapter_1/01_factorial.cpp)             |
| Matrix Addition       | [Readme](source/chapter_1/02_matrix_add.md)            | [Code](source/chapter_1/02_matrix_add.cpp)            |
| Bubble Sort           | [Readme](source/chapter_1/03_bubble_sort.md)           | [Code](source/chapter_1/03_bubble_sort.cpp)           |
| Linear Search         | [Readme](source/chapter_1/04_linear_search.md)         | [Code](source/chapter_1/04_linear_search.cpp)         |
| Max Element           | [Readme](source/chapter_1/05_max_element.md)           | [Code](source/chapter_1/05_max_element.cpp)           |
| Fibonacci Sequence    | [Readme](source/chapter_1/06_fibonacci.md)             | [Code](source/chapter_1/06_fibonacci.cpp)             |
| Tower of Hanoi        | [Readme](source/chapter_1/07_hanoi_tower.md)           | [Code](source/chapter_1/07_hanoi_tower.cpp)           |
|                       | **— [Chapter 2](source/chapter_2/) —**                 |                                                       |
| Array Simple          | [Readme](source/chapter_2/01_array_simple.md)          | [Code](source/chapter_2/01_array_simple.cpp)          |
| Array Addresses       | [Readme](source/chapter_2/02_array_addresses.md)       | [Code](source/chapter_2/02_array_addresses.cpp)       |
| Address Formula       | [Readme](source/chapter_2/03_address_formula.md)       | [Code](source/chapter_2/03_address_formula.cpp)       |
| Linear Search         | [Readme](source/chapter_2/04_linear_search.md)         | [Code](source/chapter_2/04_linear_search.cpp)         |
| Binary Search         | [Readme](source/chapter_2/05_binary_search.md)         | [Code](source/chapter_2/05_binary_search.cpp)         |
| Matrix Addresses      | [Readme](source/chapter_2/06_matrix_addresses.md)      | [Code](source/chapter_2/06_matrix_addresses.cpp)      |
| Sparse Matrix         | [Readme](source/chapter_2/07_sparse_matrix.md)         | [Code](source/chapter_2/07_sparse_matrix.cpp)         |
|                       | **— [Chapter 3](source/chapter_3/) —**                 |                                                       |
| Stack Array           | [Readme](source/chapter_3/01_stack_array.md)           | [Code](source/chapter_3/01_stack_array.cpp)           |
| Stack Under Flow      | [Readme](source/chapter_3/02_stack_under_flow.md)      | [Code](source/chapter_3/02_stack_under_flow.cpp)      |
| Postfix Expression    | [Readme](source/chapter_3/03_postfix_expression.md)    | [Code](source/chapter_3/03_postfix_expression.cpp)    |
| Infix to Postfix      | [Readme](source/chapter_3/04_infix_to_postfix.md)      | [Code](source/chapter_3/04_infix_to_postfix.cpp)      |
| Recursive Subroutines | [Readme](source/chapter_3/05_recursive_subroutines.md) | [Code](source/chapter_3/05_recursive_subroutines.cpp) |
|                       | **— [Chapter 4](source/chapter_4/) —**                 |                                                       |
| Queue (FIFO / LIFO)   | [Readme](source/chapter_4/01_queue_fifo_lifo.md)       | [Code](source/chapter_4/01_queue_fifo_lifo.cpp)       |
| Queue Operations      | [Readme](source/chapter_4/02_queue_ops.md)             | [Code](source/chapter_4/02_queue_ops.cpp)             |
| Queue Display         | [Readme](source/chapter_4/03_queue_display.md)         | [Code](source/chapter_4/03_queue_display.cpp)         |
| Linked List           | [Readme](source/chapter_4/04_linked_list.md)           | [Code](source/chapter_4/04_linked_list.cpp)           |
| Loops                 | [Readme](source/chapter_4/05_loops.md)                 | [Code](source/chapter_4/05_loops.cpp)                 |
| List Traversal        | [Readme](source/chapter_4/06_list_traversal.md)        | [Code](source/chapter_4/06_list_traversal.cpp)        |

---

### ساختار کلی هر درس

هر درس در پروژه با **یک فایل C++ مستقل** نوشته شده و به جای گرفتن ورودی تعاملی (`cin`)، **ورودی‌ها از آرگیومنت‌های خط فرمان** (`argv`) دریافت می‌شوند.

برای مثال:

```bash
./01_factorial 5
```

در این حالت:

- `argv[0]` = مسیر برنامه (`./01_factorial`)
- `argv[1]` = `5` (عدد مورد نظر برای محاسبه فاکتوریل)

---

### آرگیومنت‌ها در برنامه‌ها

- **اعداد ساده**: مثل فاکتوریل یا فیبوناچی، تنها یک مقدار نیاز دارند.

- **آرایه‌ها و لیست‌ها**: عناصر آرایه یا لیست پیوندی به صورت **دنباله‌ای از آرگیومنت‌ها** پاس می‌شوند.

  - `argv[1]` = طول آرایه (`5`)
  - `argv[2..6]` = عناصر آرایه (`10, 20, 15, 30, 25`)

- **صف و عملیات‌ها**: در مثال Queue، ممکن است یک سری دستورات مثل `dequeue` و `pop` به عنوان آرگیومنت پاس شوند:

  - مثال: `01_queue_fifo_lifo 10 20 30 dequeue 40`

---

### هندل کردن آرایه‌ها و لیست‌ها

- در برنامه C++، معمولاً مراحل زیر انجام می‌شود:

1. **خواندن طول لیست/آرایه** از `argv[1]`
2. **ایجاد آرایه/لیست** با طول مشخص
3. **پر کردن عناصر** از باقی آرگیومنت‌ها (`argv[2..n]`)

   ```cpp
   for (int i = 0; i < n; i++)
       arr[i] = std::atoi(argv[2 + i]);
   ```

4. عملیات موردنظر (مرتب‌سازی، پیمایش، نمایش، …)
5. چاپ خروجی نهایی روی `stdout` (یک خط یا چند خط بسته به درس)

---

### مزیت این روش

- **بدون نیاز به ورودی تعاملی** → مناسب تست خودکار با Python
- هر خروجی **قابل assert مستقیم** است
- مدیریت آرایه‌ها و لیست‌ها کاملاً **سلسله‌مراتبی و ساده** است: طول + عناصر

---

## مراحل پیاده سازی

> مراحل 3 به بعد برای تست اختیاری میباشد.

1. ابتدا کمپایلر مربوط به سیستم عامل خود را نصب کنید:
   [Download](https://jmeubank.github.io/tdm-gcc/download/)

2. داخل CMD از نصب آن اطمینان حاصل کنید

   دستور:

   ```bash
   g++ --version
   ```

   نتیجه:

   ```output
   g++.exe (tdm64-1) 10.3.0
   ```

3. افزونه C++ را در vsCode نصب میکنیم.

   - در این مرحله میتوانیم کد هارا از مسیر source کامپایل و اجرا کنیم

4. برای کامپایل کردن و تست دست جمعی python را نصب میکنیم.

5. با استفاده از pip کتابخانه های مورد نیاز را نصب کنید:

   دستور:

   ```bash
   pip install -r requirements.txt
   ```

6. با اجرا کردن فایل `compile.py` تمامی فایل ها کمپایل شده و در پوشه `build` قرار میگیرند.

   دستور:

   ```bash
   python ./compile.py
   ```

7. حال با استفاده از دستور pytest میتوانید هر فصل را تست کنید:
   ```bash
   python -m pytest -v
   ```
   نتیجه:
   ```text
   test/test_chapter_1.py::test_factorial PASSED
   test/test_chapter_1.py::test_matrix_add PASSED
   test/test_chapter_1.py::test_bubble_sort PASSED
   test/test_chapter_1.py::test_linear_search PASSED
   test/test_chapter_1.py::test_max_element PASSED
   ...
   ```

---

## توضیح درباره فایل **Compile**

- این فایل مسئول **کامپایل کردن تمام فایل‌های درس‌ها** است.
- از `g++` برای تولید فایل‌های اجرایی (`.exe`) استفاده می‌کند.
- فایل خروجی در مسیر `build/` ذخیره می‌شود.
- در صورت بروز خطا هنگام کامپایل، فایل جزئیات خطا را چاپ می‌کند.

---

## توضیح درباره فایل **Test**

- فایل Test مسئول **اجرای خودکار برنامه‌ها با ورودی‌های مشخص** و بررسی خروجی است.
- از کتابخانه `pytest` برای دریافت نتایج تست ها به صورت یکجا استفاده شده است.

  1. برنامه اجرا می‌شود
  2. خروجی با نتیجه‌ی مورد انتظار مقایسه می‌شود

- در صورت موفقیت تست، پیام `PASSED` و در غیر این صورت پیام خطا نمایش داده می‌شود.

نمونه یکی از تست ها:

```python
def test_postfix_expression():
    assert ch_3_postfix_expression.run('1', '1', '+') == '2'
```

- در مثال بالا اسکریپت عبارت پسوندی اجرا شده و مقادیر `+11` به ماشین میدهد و در انتها جواب ماشین با عدد `2` مقایسه شده و در صورت مقایرت خطا چاپ میشود

---

## جدول فایل های تست

| Chapter   | Test Files                          |
| --------- | ----------------------------------- |
| Chapter 1 | [Test File](test/test_chapter_1.py) |
| Chapter 2 | [Test File](test/test_chapter_2.py) |
| Chapter 3 | [Test File](test/test_chapter_3.py) |
| Chapter 4 | [Test File](test/test_chapter_4.py) |

---

## تصویر تست های انجام شده از تمامی دروس

<div style="text-align: center;">
    <img src="screenshots/tested.gif" width="400">
</div>

---

### ✅ نکات مهم

- قبل از اجرای هر درس، مطمئن شوید که مسیر **build/** وجود دارد.
- از Python 3 برای اجرای `LessonScript` استفاده کنید.
- در Windows، هنگام استفاده از `*` در Postfix، یا آن را **quoted** وارد کنید یا از جایگزین مثل `'x'` استفاده کنید.

</div>
