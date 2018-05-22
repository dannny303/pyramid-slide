from helper import alphabet_position, rotate_character

def encrypt(text, rot):
    answer = ""
    for char in text:
        answer += rotate_character(char,rot)
    return (answer)

def main():
    text = input("Encrypt a message:\n")
    rot = input("Rotate Caesar Cipher by how many?:\n")
    print(encrypt(text, int(rot)))

if __name__ == "__main__":
    main()
