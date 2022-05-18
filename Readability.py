from cs50 import get_string
input = get_string("Text: ")

def main():

    L = round((count_letters(input)/count_words(input))*100,2)
    S = round((count_sentences(input)/count_words(input))*100,2)
    n = round(0.0588 * L - 0.296 * S - 15.8)
    if n < 1:
        print("Before Grade 1...")
    elif n > 16:
        print("Grade 16+")
    else:
        print(f"Grade {n}")

def count_sentences(x):
    S = 0
    for i in range(len(x)):
        if x[i] in (".","?","!"):
            S += 1
    return S

def count_words(x):
    W = 1
    for i in range(len(x)):
        if x[i] == " ":
            W += 1
    return W

def count_letters(x):
    L = int(len(x))
    spaces = 0
    for i in range(len(x)):
        if x[i] in (" ",",","!",".","?","'",":","-","/"):
            spaces += 1
    L = L - spaces
    return L

main()
