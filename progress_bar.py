import sys, time
from colors import *

def progress_bar(task, duration=1.5):
    print(f"\n{CYAN}{BOLD}{task}{RESET}")
    for i in range(0, 101, 8):
        bar = GREEN + "#" * (i // 8) + "-" * (12 - i // 8) + RESET
        sys.stdout.write(f"\r {YELLOW}[{bar}]{RESET} {i}%")
        sys.stdout.flush()
        time.sleep(duration / 12)
    print()

def section(title):
    print("\n" + BLUE + "=" * 65 + RESET)
    print(f"{BOLD}{YELLOW}== {title}{RESET}")
    print(BLUE + "=" * 65 + RESET)

def info(msg):
    print(f" {GREEN}✔{RESET} {msg}")

def warn(msg):
    print(f" {YELLOW}!{RESET} {msg}")
