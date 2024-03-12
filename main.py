def are_samosas_sufficient(guests, dough_sheets, minced_meat, kiri_cheese, requests):
    total_meat_samosas = sum(request[0] for request in requests)
    total_cheese_samosas = sum(request[1] for request in requests)

    meat_needed = total_meat_samosas * 5  # 5 غرامات لحم لكل سمبوسة لحم
    cheese_needed = total_cheese_samosas * 0.5  # نصف قطعة جبن كيري لكل سمبوسة جبن

    if dough_sheets < (total_meat_samosas + total_cheese_samosas) or minced_meat < meat_needed or kiri_cheese < cheese_needed:
        return "ما يكفي"
    else:
        return "يكفي"

# Collect input
guests = int(input("أدخل العدد الإجمالي للضيوف: "))
dough_sheets = int(input("أدخل عدد رقائق السمبوسة المتاحة: "))
minced_meat = int(input("أدخل كمية اللحم المفروم المتاحة بالجرام: "))
kiri_cheese = int(input("أدخل عدد قطع جبن الكيري المتاحة: "))

requests_count = int(input("أدخل عدد الطلبات: "))
requests = []
for _ in range(requests_count):
    meat_samosas, cheese_samosas = map(int, input("أدخل عدد سمبوسة اللحم والجبن المطلوبة مفصولة بمسافة لكل طلب: ").split())
    requests.append([meat_samosas, cheese_samosas])

# Call the function and print the result
result = are_samosas_sufficient(guests, dough_sheets, minced_meat, kiri_cheese, requests)
print(result)
