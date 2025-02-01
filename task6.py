'''
Завдання 6. Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм 
динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах 
обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — 
назва страви, а значення — це словник з вартістю та калорійністю.

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення 
калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює 
оптимальний набір страв для максимізації калорійності при заданому бюджеті.'''

class Item:
    def __init__(self, calories, value, name):
        self.calories = calories
        self.value = value
        self.name = name
        self.ratio = value / calories

# greedy_algorithm
def knapSack(items: list[Item], budget: int) -> int:
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_calories = 0
    food = []
    for item in items:
        if budget >= item.value:
            budget -= item.value
            total_calories += item.calories
            food.append(item.name)
    return total_calories, food, budget

def find_knapsack_top(items, budget,  i=0, lookup= None):
    lookup = {} if lookup is None else lookup
    if (i,budget) in lookup:
        return lookup[(i,budget)]

    if len(items) == i or budget < 0:
        return 0
    elif (items[i].value > budget):
        return find_knapsack_top(items, budget, i+1, lookup)
    else:
        lookup[(i,budget)] = max(items[i].calories+ find_knapsack_top(items,budget-items[i].value,i+1,lookup),
                            find_knapsack_top(items,budget,i+1, lookup))
        return lookup[(i,budget)]

# dynamic algorithm
'''def dynamic_programming(items, budget, lookup=None):
    lookup = {} if lookup is None else lookup  # Initialize lookup if None

    # Base cases:
    if budget == 0:
        return {}
    if budget < 0:  # Changed base case
        return None 
    if budget in lookup:
        return lookup[budget]  
    
    max_calories = 0
    best_combination = None

    for item in items:
        remaining_amount = budget - item.value
        
        result = dynamic_programming(items, remaining_amount, lookup)  # Recursive call

        if result is not None:
            current_calories = item.calories + (sum(item.calories for item in result.values()) if result else 0) 
            
            if current_calories > max_calories:
                max_calories = current_calories
                best_combination = {item.name: item}  # Add current item to combination
                best_combination.update(result)  # Update with previous result


    lookup[budget] = best_combination

    return  best_combination

'''
def main():
    # Дані предметів
    #items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    items = {
        "pizza": {"cost": 50, "calories": 300},
         "hamburger": {"cost": 40, "calories": 250},
         "hot-dog": {"cost": 30, "calories": 200},
         "pepsi": {"cost": 10, "calories": 100},
         "cola": {"cost": 15, "calories": 220},
         "potato": {"cost": 25, "calories": 350}
    }

    menu = []
    for key, value in items.items():
        menu.append(Item(value["calories"], value["cost"], key))


    # Місткість рюкзака
    while True:
        user_input = input("Enter your budget (or type 'q' to quit): ").strip()
        print(" ")
            
        if user_input.lower() == 'q':  # Allow quitting
            print("Goodbye!")
            break

        try:
            budget = 120
            lookup = {}
            budget = int(user_input)
            print(f"Our menu: {items}")
            total_calories, food, change = knapSack(menu, budget)
            print(" ")
            print("We use greedy algorithm to plan your menu!")
            print(f"You can receive {total_calories} calories eating {food}. Your change is {change}")  # 160

            print(" ")
            print("Using dynamic algorithm to plan your menu:")

            best_food  = find_knapsack_top(menu, budget)
            print(best_food)
            
            ''' if best_food:
                print("Best food combination within budget", budget)
                total_calories = 0

                for food_name, food_item in best_food.items():
                    print(f"- {food_name} (Calories: {food_item.calories}, Cost: {food_item.value})")
                    total_calories += food_item.calories
                print("Total calories:", total_calories)
            else:
                print("No combination found within the budget.")'''
            #print(f"You can receive {total_calories} calories eating {food}. Your change is {change}")  # 160

        except ValueError:
            print("❌ Invalid input! Please enter a number or type 'q' to quit.")
   

if __name__ == "__main__":
    main()