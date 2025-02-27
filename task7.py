'''
Звдання 7. Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, 
які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, 
які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі 
симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені 
за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в 
таблиці вище.
'''

import random
import matplotlib.pyplot as plt
import numpy as np

def generate_readme(probability_estimates, analytical_probability):
    with open("readme.md", "w") as f:
        f.write("# Comparative Analysis: Analytical Method vs Monte-Carlo\n\n")

        # Introduction
        f.write("## Introduction\n\n")
        f.write("This README compares the results of calculating the probability distribution of the sum of two dice using two distinct methods: the analytical method and the Monte Carlo method. The analytical method derives probabilities directly from combinatorial principles, providing exact results. In contrast, the Monte Carlo method relies on repeated random sampling to estimate probabilities. This simulation involves a large number of virtual dice rolls, and the observed frequencies of different sums are used to approximate the true probabilities. We will analyze how closely the Monte Carlo estimates converge to the analytical probabilities, highlighting the strengths and limitations of each approach. This comparison serves to illustrate the utility of the Monte Carlo method, especially in scenarios where analytical solutions are complex or intractable.\n\n")

        # Comparative Analysis: Analytical Method vs Monte-Carlo
        f.write("## Probabilities received:\n\n")
        f.write("|    SUM OF TWO DICE      |  probability_estimates  |  analytical_probability  |\n")
        f.write("|-------------------------|-------------------------|--------------------------|\n")
        for i in range(len(probability_estimates)):
            f.write(f"|           {i + 2}             |        {probability_estimates[i]}            |        {analytical_probability[i]}           |\n")

        # Conclusion
        f.write("\n\n## Conclusion\n\n")
        f.write("No significant differences between 2 methods were observed (num_samples = 100000).\n\n")
        f.write("However, it's important to performe a large number of experimets to achieve a good result.")



def monte_carlo_pi(num_samples, a = 1, b = 6):
    # 1. Визначення моделі або системи.
    counters = [0] * 11

    # 2. Генерація випадкових вхідних даних
    for _ in range(num_samples):
        x = int(random.uniform(a, b))
        y = int(random.uniform(a, b))
        i = x + y

        counters[i-2] += 1

    # 4. Агрегування та аналіз результатів
    
    for i in range(len(counters)):
        counters[i] = counters[i]  * 100 / num_samples
   
    return counters

def main():
    analytical_probability = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
    print(f"Аналітичні значення: {analytical_probability}")

    # Задаємо кількість випадкових точок
    num_samples = 100000
    a = 1
    b = 7

    # Розраховувємо ймовірності кожної суми, виявлені за допомогою методу Монте-Карло 
    probability_estimates = monte_carlo_pi(num_samples, a, b)
    print(f"Розраховані значення: {probability_estimates}")

    generate_readme(probability_estimates, analytical_probability)

    # Візуалізуємо результати
    bar_width = 0.35  
    x_pos_analytical = np.arange(11)
    x_pos_experimental = np.arange(11) + bar_width

    plt.bar(x_pos_analytical, analytical_probability, width=bar_width, label='Analytical')
    plt.bar(x_pos_experimental, probability_estimates, width=bar_width, label='Experimental')

    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Probability (%)")
    plt.title("Probability Distribution of Dice Rolls")
    plt.text(0.0, 19.5, f'No significant differences between 2 methods', fontsize=12, color='red')
    # Custom x-axis labels
    custom_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']  
    plt.xticks(x_pos_analytical + bar_width / 2, custom_labels)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
