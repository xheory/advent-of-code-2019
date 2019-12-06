from stars import run_functions
from colorama import Fore, Style

if __name__ == "__main__":
    for index, run_function in enumerate(run_functions):
        index_str = index + 1
        print(
            f"{Fore.WHITE + Style.BRIGHT}[{Fore.YELLOW}*{Fore.GREEN}{index_str:02}{Fore.WHITE}]{Style.NORMAL} ",
            end="",
        )
        output = run_function()
        if output:
            split_output = output.split(":")
            print(
                f"{split_output[0]}:{Fore.GREEN + Style.BRIGHT}{split_output[1]}{Style.RESET_ALL}"
            )
