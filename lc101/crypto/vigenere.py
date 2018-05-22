from helper import alphabet_position, rotate_character

def encrypt(text, rot_text):
    answer = ""
    cypkey = []
    for char in rot_text:
        cypkey.append(alphabet_position(char))
    count = 0
    for char in text:
        length = count % len(cypkey)
        count += 1
        cyphered = rotate_character(char, cypkey[length])
        answer += cyphered
    return answer

def main():
    text = input("Encrypt a message:\n")
    rot_text = input("Choose a Cypher Key: \n")
    print(encrypt(text,(rot_text)))

if __name__ == "__main__":
    main()
