import random

def guess_the_number(total_tries, start_range, end_range):
    if start_range > end_range:
        start_range, end_range = end_range, start_range

    random_number = random.randint(start_range, end_range)
    try_count = 0
    success_message = "Awesome! You guessed correctly"
    failure_message = "Sorry! No more retries left"
    miss_message = "Oops! That's incorrect"

    num_tries = 0
    while num_tries < total_tries:
        attempt = int(input("Guess the number: "))

        if attempt == random_number:
            print(success_message)
            return
        print(miss_message)
        if attempt < random_number:
            print("Go higher!")
        else:
            print("Go lower!")
        num_tries += 1
    print(failure_message)

total_tries = 10
start_range = 1
end_range = 1000
guess_the_number(total_tries, start_range, end_range)
