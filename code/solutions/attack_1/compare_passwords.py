def compare_passwords(ground_truth, test_password):
    """
    Compare two passwords and return the total time taken to compare.
    If the passwords are of different lengths, the function returns 0.
    """
    total_time = 0

    if len(ground_truth) != len(test_password):
        return total_time

    for i in range(len(ground_truth)):
        if ground_truth[i] != test_password[i]:
            return total_time
        total_time += 1

    return total_time
