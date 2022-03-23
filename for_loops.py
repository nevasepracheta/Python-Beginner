friends = ["Jim", "Pam", "Kevin"]

for index in range(len(friends)): #Last index here will be len-1 and first index being 0
    if index == 0:
        print("Welcome to office: Meet the members")
    print(friends[index])

def raise_to_power(base_number, power_number):
    result = 1
    for index in range(power_number):
        result = result * base_number
    return result

print(raise_to_power(24, 3))
