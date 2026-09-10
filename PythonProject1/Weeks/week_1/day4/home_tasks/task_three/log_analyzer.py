# анализатор лога, считает кол-во запросов с каждого ip, считает каждый статус код и сохраняет репорт
ip_result = {}
status_result = {}
status_index = 6
ip_index = 0

with open("server.log", 'r') as file:
    for line in file:
        line = line.split(" ")
        if not line:
            continue
        if len(line) < 7:
            continue

        ip = line[ip_index]
        status = line[status_index]

        status_result[status] = status_result.get(status, 0) + 1
        ip_result[ip] = ip_result.get(ip, 0) + 1

# with open('report.txt', 'w') as file:
#     file.write(str(ip_result))
#     file.write(str(status_result))

    # Формируем отчёт в читаемом виде
    with open("report.txt", "w", encoding="utf-8") as file:
        file.write("IP counts:\n")
        for ip, count in ip_result.items():
            file.write(f"{ip}: {count}\n")

        file.write("\nStatus codes counts:\n")
        for status, count in status_result.items():
            file.write(f"{status}: {count}\n")
