# Function
# Pertamabahn
def tambah(a, b):
    return a + b
# Pengurangan
def kurang(a, b):
    return a - b
# Perkalian
def kali(a, b):
    return a * b
# Pembagian
def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error!"

# Menu
def menu():
    print("Choose your operation:")
    print("1. Sum (+)")
    print("2. Sub (-)")
    print("3. Mul (x)")
    print("4. Div (/)")

    pilihan = input("Input Menu: ")
    if pilihan in ['1', '2', '3', '4']:
        num1 = float(input("A: "))
        num2 = float(input("B: "))

        if pilihan == '1':
            print(f"Hasil: {num1} + {num2} = {tambah(num1, num2)}")
        elif pilihan == '2':
            print(f"Hasil: {num1} - {num2} = {kurang(num1, num2)}")
        elif pilihan == '3':
            print(f"Hasil: {num1} * {num2} = {kali(num1, num2)}")
        elif pilihan == '4':
            print(f"Hasil: {num1} / {num2} = {bagi(num1, num2)}")

# Mengulang program / Keluar
if __name__ == "__main__":
    while True:
        menu()
        lagi = input("Count again? ... (y/n) ")
        if lagi.lower() != 'y':
            break