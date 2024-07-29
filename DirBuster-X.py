import requests
import sys
import time

def buster(link, wordlist_path):
    try:
        with open(wordlist_path, 'r') as wordlist:
            for word in wordlist:
                word = word.strip()
                r = requests.get(f"{link}/{word}")
                if r.status_code == 200:
                    print(f"/{word}")
    except FileNotFoundError:
        print(f"The file {wordlist_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def animated_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after the text is printed

def starting_message():
    dots = ['.', '..', '...']
    for dot in dots:
            sys.stdout.write(f'\rDirectory Fuzzing Started{dot}')
            sys.stdout.flush()
            time.sleep(0.3)

animated_print("\n        DIRBUSTER-X (--version 1.2)", 0.05)
print("\n")

link = input("Enter the URL: ").lower()
filename = input("Enter the path of the wordlist: ").lower()

starting_message()

print("\n")

buster(link, filename)

print("\nDirectory busting completed.")