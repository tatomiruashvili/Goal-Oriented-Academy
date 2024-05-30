# ნულიდან ათამდე კენტი რიცხვების ჯამი
x = 0
odd_sum=0
while x <= 10:
    if x % 2 != 0:
        odd_sum += x
    x += 1
print(f"Sum Of Numbers From Zero To ten is {odd_sum}")