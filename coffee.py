num_orders = int(input("Введите количество заказов кофе: "))
orders = []
all_orders_money = 0
all_colleague_money = 0

for i in range(num_orders):
    print(f"\n🛍️ Заказ {i + 1}:")
    cost = float(input("Введите стоимость заказа: "))
    all_orders_money += cost
    num_people = int(input("Введите количество людей, которые будут скидываться за этот заказ: "))
    orders.append((cost, num_people))

total_people = int(input("\nВведите общее количество людей, которые будут скидываться: "))

contributions = {i: 0 for i in range(1, total_people + 1)}

for i, (cost, num_people) in enumerate(orders):
    print(f"\n🛍️ Заказ {i + 1} стоимостью {cost} рублей:")
    participants = input(f"Введите номера людей (через пробел), которые скидываются на этот заказ: ").split()
    participants = [int(p) for p in participants]

    cost_per_person = cost / num_people

    for p in participants:
        contributions[p] += cost_per_person

print("\nСумма, которую должен сдать каждый человек:")
for person, contribution in contributions.items():
    print(f"🤠 Человек {person}: {contribution:.2f} рублей")
    all_colleague_money += contribution

print(f"\nВсе заказы вышли на сумму {all_orders_money:.2f} рублей.")
print(f"Собрал с коллег {all_colleague_money:.2f} рублей.")