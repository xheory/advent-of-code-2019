from stars.star1 import run as run_star1

run_functions = [run_star1]

if __name__ == "__main__":
    for index, run_function in enumerate(run_functions):
        print(f"[*{index + 1}] {run_function()}")
