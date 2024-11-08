def gaussian_elimination_with_inverse(A, f): # Оголошення функції
    # Ініціалізація змінних  
    n = len(f) #кількість рівнянь у системі
    determinant = 1 #початкове значення для обчислення детермінанта
    sign_change = 1 #змінна для відстеження зміни знаку при перестановці рядків
    is_degenerate = False # Позначення, що матриця є виродженою

    # Створення одиничної матриці
    identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    # Прямий хід, перетворюємо матрицю в трикутну
    for i in range(n):
        # Пошук найбільшого елемента у стовпці
        # вибирається рядок із найбільшим елементом у поточному стовпці
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        
        # Заміна рядків у матриці A, векторі f і одиничній матриці
        if i != max_row:
            A[i], A[max_row] = A[max_row], A[i]
            f[i], f[max_row] = f[max_row], f[i]
            identity[i], identity[max_row] = identity[max_row], identity[i]
            sign_change *= -1

        # Перевірка на нульовий елемент на діагоналі
        if A[i][i] == 0:
            if f[i] != 0:
                return "несумісна", 0, None
            is_degenerate = True
            continue
        
        # Оновлення детермінанта
        determinant *= A[i][i]

        # Прямий хід: знищення елементів під головною діагоналлю
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            f[k] -= factor * f[i]
            
            # Оновлення одиничної матриці для оберненої
            for j in range(n):
                identity[k][j] -= factor * identity[i][j]

    # Перевірка детермінанта 
    determinant *= sign_change

    if determinant == 0:
        return "вироджена", determinant, None

    # Зворотній хід: знаходження розв'язку та оберненої матриці
    x = [0] * n
    for i in range(n - 1, -1, -1):
        if A[i][i] == 0:
            continue
        x[i] = f[i] / A[i][i]
        for k in range(i - 1, -1, -1):
            factor = A[k][i] / A[i][i]
            f[k] -= A[k][i] * x[i]
            
            # Оновлення одиничної матриці для оберненої
            for j in range(n):
                identity[k][j] -= factor * identity[i][j]

        # Нормалізація рядка
        for j in range(n):
            identity[i][j] /= A[i][i]

    # Повернення результату
    if is_degenerate:
        return "сумісна, вироджена", determinant, identity

    return x, determinant, identity

# Приклад матриці A і вектора f
A = [
    [4, 1, 0, -1],
    [1, -3, 4, 0],
    [0, 3, -2, 4],
    [1, 2, -1, 3]
]

f = [4, -1, 12, -2]

# Розв'язання системи та обчислення детермінанта і оберненої матриці
result, determinant, inverse_A = gaussian_elimination_with_inverse(A, f)

# Відомий точний розв'язок
known_solution = [1, 2, 1, 2]

# Перевірка, чи система є несумісною
if isinstance(result, str):
    print(f"Система {result}.")
else:
    print("Точний розв'язок системи (x):")
    
    # Виведення результату з округленням до двох знаків після коми
    result = [round(x_i, 2) for x_i in result]
    print(result)

    # Обчислення відхилення
    deviation = [round(result[i] - known_solution[i], 2) for i in range(len(known_solution))]

    # Виведення відхилень
    print("\nВідхилення між відомим точним і отриманим розв'язком:")
    for i in range(len(deviation)):
        print(f"x{i}: відоме значення = {known_solution[i]}, отримане значення = {result[i]}, відхилення = {deviation[i]}")

    # Виведення оберненої матриці з округленням до двох знаків після коми
    print("\nОбернена матриця до A:")
    inverse_A = [[round(elem, 2) for elem in row] for row in inverse_A]
    for row in inverse_A:
        print(row)
