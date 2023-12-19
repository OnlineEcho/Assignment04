import string
from compare_passwords import compare_passwords


def timing_attack_local():
    valid_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + ".,!?_-"
    max_time = 0
    best_guess = ""

    # Test setup
    ground_truth_password = "securePassword123"

    for j in range(18):
        for k in valid_characters:
            password_guess = best_guess + k + "0" * (17 - j)
            # Try each password guess from the file
            total_time = compare_passwords(ground_truth_password, password_guess)

            # Update the guessed password if the elapsed time is higher
            if total_time > max_time:
                max_time = total_time
                best_guess += k
                break

    return best_guess, max_time