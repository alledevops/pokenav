#“Today is a great day for #battle and #catch them all. Love to #battle

sentence = input()
x = sentence.split()
unique = []


def uniqueHAS():


    for i in x:

        if i not in unique:

            unique.append(i)
        
            if i[0] == "#":
                print(i)
        

def _main_() :
    uniqueHAS()

_main_()

# RETURN TO MENU