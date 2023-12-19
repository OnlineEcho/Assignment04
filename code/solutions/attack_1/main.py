from timing_attack_local import timing_attack_local

if __name__ == "__main__":
    # testing local
    guess, t_time = timing_attack_local()
    print(f"Best guess {guess} in time {t_time}")



