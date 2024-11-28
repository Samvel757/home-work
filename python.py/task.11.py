def check_odd_even(numbers):
    odd_count = sum(1 for x in numbers if x % 2 != 0)
    even_count = len(numbers) - odd_count
    return "Нет" if odd_count > even_count else "Да"

N = int(input("Введите длину списка: "))
numbers = list(map(int, input("Введите числа через пробел: ").split()))

if len(numbers) != N:
    print("Количество введённых чисел не соответствует заданной длине списка.")
else:
    result = check_odd_even(numbers)
    print(result)