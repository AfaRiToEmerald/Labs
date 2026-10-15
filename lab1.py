coast: int = int(input("Введите количество товаров: "))
price: float = float(input("Введите цену одного товара: "))
discount: float = float(input("Введите величину скидки в %: "))

allcost: float = coast * price                         #общая цена
discount_all: float = allcost * (discount / 100.0)     #скидка в рублях
final_cost: float = allcost - discount_all         #итоговая цена

print("Итого")
print(f"общая цена товаров:{allcost:.2f}Руб.")
print(f"размер скидки:{discount_all:.2f}Руб.")
print(f"Итоговая стоимость с учётом скидки:{final_cost:.2f}Руб.")


#если что 6 задание