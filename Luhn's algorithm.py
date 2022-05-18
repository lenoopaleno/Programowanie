
from cs50 import get_string
def main():
    card_num = get_string("What's card number: ")
    check(card_num)

def name(x):
        if x[0] == "4":
            print("VISA")
        if x[0] == "5":
            print("MASTERCARD")
        if x[0] == "3":
            print("AMEX")

def check(x):
    count_f = 0
    count_s = 0
    for i in range(len(x)):
        if  i%2 == 0:
            if ((int(x[i]))*2)>=10:
                count_f = count_f + (((int(x[i]))*2)%10 + ((int(x[i]))*2)//10)
            else:
                count_f = count_f + (int(x[i]))*2
        elif i%2 == 1:
            count_s = count_s + (int(x[i]))
    count = count_s + count_f
    if count%10 == 0:
        name(x)
    else:
        print("INVALID")



main()

