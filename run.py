from stars import run_functions

if __name__ == "__main__":
    for index, run_function in enumerate(run_functions):
        print(f"[*{index + 1}] ", end="")
        output = run_function()
        if output:
            print(output)
