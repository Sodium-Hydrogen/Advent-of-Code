

numbers = []
with open('input/day3.txt') as file:
    numbers = [x for x in file.read().splitlines()]

if __name__ == "__main__":
    total = [0 for _ in numbers[0]]
    half = len(numbers)/2 
    for numstr in numbers:
        for index,byte in enumerate(numstr[::-1]):
            total[index] += bool(int(byte))
            #print(int(byte) << index, end='')
        #print()
    total = ['1' if x > half else '0'  for x in total[::-1]]

    gama = int("".join(total), 2)
    epsilon = gama ^ int("".join(['1' for x in total]), 2)
    print(f"Gama: {gama}, Epsilon: {epsilon}\nPower Comp {gama*epsilon}")
        
