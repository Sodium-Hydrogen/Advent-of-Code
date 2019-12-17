import day4pt1

passwords = []
for password in day4pt1.passwords:
    for i in range(10):
        if password.count(str(i)) == 2:
            passwords.append(password)
            break

if __name__ == '__main__':
    print(f"Day 4 pt. 2: {len(passwords)}")
