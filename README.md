
# 🖥️ Tkinter Assignment – Student Information Form

## 🎯 Objective
Create a Python Tkinter program that displays three text boxes to collect:

- Student Name
- Student ID
- Password

The **Submit button must appear only after all fields are filled**.

---

## 📌 Requirements

1. Create three input fields using Tkinter:
   - Name
   - Student ID
   - Password (use show="*" for password field)

2. The Submit button:
   - Must NOT be visible initially.
   - Must appear ONLY when all three fields contain some text.

3. Do NOT rename the required function:
   - `check_fields()`

4. Use proper Tkinter widgets:
   - Label
   - Entry
   - Button

---

## 🧪 Grading Criteria (100 Marks)

| Component | Marks |
|------------|--------|
| Three Entry fields | 30 |
| Password masked | 20 |
| check_fields function | 20 |
| Submit button appears conditionally | 30 |

---

## 🚀 How to Run

```bash
python main.py
```

---

## 💡 Hint

You can use:
- `.get()` to retrieve Entry values
- `.pack_forget()` or `.grid_remove()` to hide the button
- `.trace()` or `<KeyRelease>` event to detect typing
