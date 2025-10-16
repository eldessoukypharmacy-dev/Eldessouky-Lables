import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog
import datetime

# إعداد النافذة
root = tk.Tk()
root.title("صيدلية الدسوقي - طباعة اللابل")
root.geometry("450x500")
root.configure(bg="#E8F0FF")

# عنوان رئيسي
tk.Label(root, text="صيدلية الدسوقي", font=("Tahoma", 16, "bold"), bg="#E8F0FF", fg="#003366").pack(pady=10)
tk.Label(root, text="برنامج طباعة اللابل", font=("Tahoma", 12), bg="#E8F0FF").pack(pady=5)

# بيانات الإدخال
frame = tk.Frame(root, bg="#E8F0FF")
frame.pack(pady=10)

# القوائم
types = ["", "قرص", "أمبول", "سم", "عضل", "وريد", "كبسولة", "ملعقة", "نقطة", "بخاخة"]
qty = ["", "نصف", "1", "2", "3"]
times = ["", "مرة", "مرتين", "3 مرات", "كل 4 ساعات"]
durations = ["", "يوم", "3 أيام", "أسبوع", "أسبوعين", "3 أسابيع", "شهر"]

labels_data = []

def add_usage():
    t = type_var.get()
    q = qty_var.get()
    tm = times_var.get()
    du = dur_var.get()
    custom = custom_entry.get().strip()
    if custom:
        text = custom
    else:
        text = f"{q} {t} {tm} يوميًا {du}".strip()
    if not text.strip():
        messagebox.showwarning("تنبيه", "أدخل بيانات أو استخدام مخصص.")
        return
    labels_data.append(text)
    listbox.insert(tk.END, text)
    custom_entry.delete(0, tk.END)

def clear_all():
    labels_data.clear()
    listbox.delete(0, tk.END)

def print_labels():
    if not labels_data:
        messagebox.showwarning("تنبيه", "لا توجد بيانات للطباعة.")
        return
    copies = simpledialog.askinteger("عدد النسخ", "كم نسخة من كل استخدام؟", minvalue=1, initialvalue=1)
    include_name = name_check.get()

    output = ""
    if include_name:
        output += "صيدلية الدسوقي\n\n"
    for text in labels_data:
        output += (text + "\n") * copies
        output += "----------------\n"

    print_window = tk.Toplevel(root)
    print_window.title("معاينة الطباعة")
    text_box = tk.Text(print_window, wrap="word", font=("Tahoma", 10))
    text_box.insert("1.0", output)
    text_box.pack(expand=True, fill="both")

# عناصر الواجهة
tk.Label(frame, text="النوع:", bg="#E8F0FF").grid(row=0, column=0, padx=5, pady=5)
type_var = tk.StringVar()
ttk.Combobox(frame, textvariable=type_var, values=types, width=10).grid(row=0, column=1)

tk.Label(frame, text="الكمية:", bg="#E8F0FF").grid(row=0, column=2)
qty_var = tk.StringVar()
ttk.Combobox(frame, textvariable=qty_var, values=qty, width=10).grid(row=0, column=3)

tk.Label(frame, text="المرات:", bg="#E8F0FF").grid(row=1, column=0, padx=5, pady=5)
times_var = tk.StringVar()
ttk.Combobox(frame, textvariable=times_var, values=times, width=10).grid(row=1, column=1)

tk.Label(frame, text="المدة:", bg="#E8F0FF").grid(row=1, column=2)
dur_var = tk.StringVar()
ttk.Combobox(frame, textvariable=dur_var, values=durations, width=10).grid(row=1, column=3)

tk.Label(frame, text="استخدام مخصص:", bg="#E8F0FF").grid(row=2, column=0, padx=5, pady=5)
custom_entry = tk.Entry(frame, width=25)
custom_entry.grid(row=2, column=1, columnspan=3)

tk.Button(frame, text="إضافة", command=add_usage, bg="#0078D7", fg="white").grid(row=3, column=1, pady=10)
tk.Button(frame, text="مسح الكل", command=clear_all, bg="#999", fg="white").grid(row=3, column=2)

# قائمة الاستخدامات
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# خيارات الطباعة
name_check = tk.BooleanVar()
tk.Checkbutton(root, text="طباعة اسم الصيدلية", variable=name_check, bg="#E8F0FF").pack()

tk.Button(root, text="طباعة", command=print_labels, bg="#0055AA", fg="white", width=20).pack(pady=10)

root.mainloop()
