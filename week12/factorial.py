class Resursion:
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * Resursion.factorial(n-1)
        #END FACTORIAL
        
    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        return Resursion.fibonacci(n -1) + Resursion.fibonacci(n -2)
    #END FABONACCI
    
    def hanoi(n, from_rod, aux_rod, to_rod):
        if n == 1:
            print(f"ย้ายแผ่นดิส 1 จาก {from_rod} ไป {to_rod}")
            return
        
        Resursion.hanoi(n-1, from_rod, aux_rod, to_rod)
        print(f"ย้ายแห่งดิส {n} จาก {from_rod} ไป {to_rod}")
        Resursion.hanoi(n-1, aux_rod, to_rod, from_rod)
        #END HANOI

display = Resursion
print("5! = ",display.factorial(5))
print("----------------------------")

print("fibonacci is : ")
for i in range(10):
    print(display.fibonacci(i), end=" ")

n = 3
display.hanoi(n, "A", "B", "C")