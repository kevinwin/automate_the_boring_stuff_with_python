def collatz(number):
  number = int(number)
  if number % 2 == 0:
    print(str(number / 2))
    return number / 2
  else:
    print(number * 3 + 1)
    return number * 3 + 1
    
print('Enter number: ')
num = input()

while num != 1:
  num = collatz(num)
