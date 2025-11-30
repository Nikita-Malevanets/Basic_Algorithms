from collections import deque


def normalize(text):
    return text.lower().replace(" ", "")


def is_palindrome(text):
    chars = deque(normalize(text))

    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    return True


while True:
    text = input("Print word to check or 'exit' to quit: ")
    if text == "exit":
        break
    print(f"Word is palindrome: {is_palindrome(text)}")
