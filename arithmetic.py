# write your code here
import random


def generate():
    num = [2, 3, 4, 5, 6, 7, 8, 9]
    opl = ["+", "-", "*"]
    a = random.choice(num)
    b = random.choice(num)
    op = random.choice(opl)
    return str(a) + " " + op + " " + str(b)


def generate_int():
    ints = [i for i in range(11, 30)]
    a = random.choice(ints)
    return a


def calculator(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b


def compare(guess, answer):
    if guess == answer:
        return "Right!"
    else:
        return "Wrong!"


def squares(x):
    return x ** 2


def file_save(names, marks, level):
    with open("results.txt", 'a', encoding='utf-8') as f:
        if level == 1:
            f.write(f"{names}: {marks}/5 in level {level} (simple operations with numbers 2-9)\n")
        else:
            f.write(f"{names}: {marks}/5 in level {level} (integral squares of 11-29)\n")
    f.close()


if __name__ == "__main__":
    # ans
    while True:
        try:
            choice = int(input("Which level do you want? Enter a number:"))
        except ValueError:
            print("Incorrect format.")
        if 1 <= choice <= 2:
            if choice == 1:
                n, correct = 0, 0
                while n < 5:
                    my_input = generate()
                    print(my_input)
                    input_l = list(my_input.split())
                    result = calculator(int(input_l[0]), input_l[1], int(input_l[2]))
                    while True:
                        try:
                            user_input = int(input())
                        except ValueError:
                            print("Incorrect format.")
                        else:
                            ans = compare(user_input, result)
                            print(ans)
                            if ans == "Right!":
                                correct += 1
                            break
                    n += 1
                print(f"Your mark is {correct}/5.")
                save = input("Would you like to save your result to the file?Enter yes or no.")
                yes = ["yes", "YES", "y", "Yes"]
                if save in yes:
                    name = input("What is your name?")
                    file_save(name, correct, 1)
                    print('The results are saved in "results.txt"')
                    break
                else:
                    break
            else:
                n, correct = 0, 0
                while n < 5:
                    my_input = generate_int()
                    print(my_input)
                    result = squares(my_input)
                    while True:
                        try:
                            user_input = int(input())
                        except ValueError:
                            print("Wrong format! Try again.")
                        else:
                            ans = compare(user_input, result)
                            print(ans)
                            if ans == "Right!":
                                correct += 1
                            break
                    n += 1
                print(f"Your mark is {correct}/5.")
                save = input("Would you like to save your result to the file?Enter yes or no.")
                yes = ["yes", "YES", "y", "Yes"]
                if save in yes:
                    name = input("What is your name?")
                    file_save(name, correct, 2)
                    print("The results are saved in 'results.txt'")
                    break
                else:
                    break
        else:
            print("Incorrect Format.")
