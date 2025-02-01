'''
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево 
Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість 
вказати рівень рекурсії.
'''

import turtle

def draw_pythagorean_tree(level, length):
    if level == 0:
        return
    try:
        turtle.forward(length)
        turtle.left(45)
        draw_pythagorean_tree(level - 1, length * 0.7)  # Зменшуємо довжину для наступного рівня
        turtle.right(90)
        draw_pythagorean_tree(level - 1, length * 0.7)
        turtle.left(45)
        turtle.backward(length)  # Повертаємося назад до початкової точки
    except turtle.Terminator:
        print("Terminated by you! Goodbye!")
        exit()


def main():
    while True:
        # Отримання рівня рекурсії від користувача
        level_str = input("Введіть рівень рекурсії: (або введіть 'q' для завершення роботи): ").strip()
        print(" ")
            
        if level_str.lower() == 'q':  # Allow quitting
            print("Goodbye!")
            break

        try:
            level = int(level_str)
            if level < 0:
                print("❌ Invalid input! Please enter a non-negative integer.")
                continue
            else:
                # Налаштування черепашки
                turtle.speed(0)  # Максимальна швидкість
                turtle.penup()
                turtle.goto(0, -100)  # Початкова позиція
                turtle.pendown()
                turtle.left(90)  # Повертаємо черепашку вгору

                # Малювання дерева Піфагора
                draw_pythagorean_tree(level, 120)  # Початкова довжина сторони квадрата - 120

                turtle.done()  # Завершення роботи черепашки

                break 
        except ValueError:
            print("❌ Invalid input! Please enter an integer-number or type 'q' to quit.")

if __name__ == "__main__":
    main()