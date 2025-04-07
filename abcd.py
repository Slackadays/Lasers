def calcabcd(type, param) -> list:
    if type == 1:
        return [1, param, 0, 1]
    elif type == 2:
        return [1, 0, -1 / param, 1]

abcds = []

def addabcd():
    print("Choose an option:")
    print("1. Propagation")
    print("2. Thin lens")

    abcdtype = int(input("Your choice: "))

    param = 0

    if abcdtype == 1:
        param = float(input("Enter the length L of the free space: "))
    elif abcdtype == 2:
        param = float(input("Enter the focal length f of the lens: "))
        
    abcd = calcabcd(abcdtype, param)

    abcds.append(abcd)

    print("Excellent! I've just added your matrix.")

addabcd()

while True:
    print("Do you want to add another ABCD matrix?")
    print("1. Yes")
    print("2. No")

    choice = int(input("Your choice: "))

    if choice == 1:
        addabcd()
    elif choice == 2:
        break

print("Here are your shiny new ABCD matrices!")

for abcd in abcds:
    print("[", abcd[0], abcd[1], "]")
    print("[", abcd[2], abcd[3], "]")
    print("-----")

def mulabcds(first: list, second: list) -> list:
    a = first[0] * second[0] + first[1] * second[2]
    b = first[0] * second[1] + first[1] * second[3]
    c = first[2] * second[0] + first[3] * second[2]
    d = first[2] * second[1] + first[3] * second[3]

    return [a, b, c, d]

print("Here's all your matrices multiplied together!")

if len(abcds) > 1:
    while len(abcds) > 1:
        abcds[0] = mulabcds(abcds[0], abcds[1])
        abcds.pop(1)

print("[", abcds[0][0], abcds[0][1], "]")
print("[", abcds[0][2], abcds[0][3], "]")