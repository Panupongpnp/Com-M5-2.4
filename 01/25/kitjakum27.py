#1
def add_numbers(A,B):
    return A + B

#2
def square_number(A):
    return A ** 2

#3
def sum_list(A):
    return (sum(A) ** 2)

#4
def sum_str(STR1,STR2,STR3):
    return STR1 + STR2 + STR3

#5
def discount(PRICE,DISCOUNT):
    return PRICE - (PRICE * (DISCOUNT / 100))

print(add_numbers(5,2))
print(square_number(10))
print(sum_list([1,2,3,4]))
print(sum_str("Hello ", "World", "!"))
print(discount(100,10))
