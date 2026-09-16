[33mcommit 71ed7538aa0b2359caadddaced1280ec7145d25b[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmaster[m[33m)[m
Author: AlexSvb <14aadldex@gmail.com>
Date:   Thu Sep 10 16:06:34 2026 +0300

    modified: added deleting method

[1mdiff --git a/PythonProject1/Weeks/week_2/day2/modules_packages/hw/phone_book/main.py b/PythonProject1/Weeks/week_2/day2/modules_packages/hw/phone_book/main.py[m
[1mindex a1feeb5..cc69a77 100644[m
[1m--- a/PythonProject1/Weeks/week_2/day2/modules_packages/hw/phone_book/main.py[m
[1m+++ b/PythonProject1/Weeks/week_2/day2/modules_packages/hw/phone_book/main.py[m
[36m@@ -1,10 +1,12 @@[m
[31m-from utils import read_json_book,safe_to_json,get_name_phone[m
[32m+[m[32mfrom utils import read_json_book, safe_to_json, get_name_phone[m
[32m+[m
 [m
 def add_contact(name, number):[m
     ph_book = read_json_book()[m
     ph_book[name] = number[m
     safe_to_json(ph_book)[m
 [m
[32m+[m
 def find_contact():[m
     searchable_contact = {}[m
     name = input("Введите имя: ")[m
[36m@@ -14,6 +16,7 @@[m [mdef find_contact():[m
             searchable_contact[key] = json_phone_book[key][m
     return searchable_contact[m
 [m
[32m+[m
 def main():[m
     flag = True[m
     while flag:[m
[36m@@ -39,5 +42,9 @@[m [mdef main():[m
         else:[m
             print("введено некорректное значение. попробуйте еще раз.")[m
 [m
[32m+[m
[32m+[m[32mdef delete_contact():[m
[32m+[m[32m    print("delete_contact")[m
[32m+[m
 if __name__ == '__main__':[m
[31m-    main()[m
\ No newline at end of file[m
[32m+[m[32m    main()[m
