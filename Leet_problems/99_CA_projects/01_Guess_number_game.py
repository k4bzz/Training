import random

# Define shit
start = 1
end = 100
score = 1000
wrong_tries = []

# Generate the secret number
secret = random.randint(start, end)


# Check the input
def check_user_input(limit_start, limit_end):

    clean_value = None
    check_pass = False
    limit = list(range(limit_start, limit_end+1))

    while not check_pass:
        clean_value = input(f"Enter an INT number in range of {limit_start} and {limit_end}: ")
        try:
            if int(clean_value) in limit:
                check_pass = True
                clean_value = int(clean_value)
            else:
                print(f"Not in range of {limit_start} - {limit_end}")
        except ValueError:
            print("Don't be a punk... input is not an INT number")
    return clean_value


run = 1
checked_value = check_user_input(start, end)

# Compare numbers
while checked_value != secret:
    # print(f"Checked value = {checked_value}")
    wrong_tries.append(checked_value)
    if checked_value > secret:
        print(f"Lower")
    elif checked_value < secret:
        print(f"Higher")
    score = score - 10
    run += 1

    checked_value = check_user_input(start, end)

print(f"""
You won punk! Your score is: {score}
It took you only {run} tries!
You tried these numbers {wrong_tries}
""")
