input = "264360-746325"


passwords = []
password = input[:input.find("-")]
while int(password) <= int(input[input.find("-")+1:]):
    prev = -1
    for i, val in enumerate(password):
        if int(val) < prev:
            password = password[:i] + password[i-1]*(len(password)-i)
            break
        prev = int(val)
    if int(password) <= int(input[input.find("-")+1:]):
        for i in range(len(password)-1):
            if password[i] == password[i+1]:
                passwords.append(password)
                break

        password = str(int(password) + 1)


if __name__ == '__main__':
    print(f"Day 4 pt. 1: {len(passwords)}")
